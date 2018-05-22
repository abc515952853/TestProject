import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import redis
import time
import json

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
r = redis.Redis(connection_pool=pool)

from tornado.options import define, options
define("port", default=555, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json; charset=UTF-8')

class LoginHandler(BaseHandler):  ##登录-------------------------------ok
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        self.DBCheckUserName(username, password)
    def DBCheckUserName(self,username,password):   ##判断登录
        if username and password:
                if r.hexists("user", username):
                    DBpasword = r.hget('user',username)
                    if(DBpasword == password):
                        return self.write({'status':1, 'data':{'token': ''}, 'msg':'登录成功！'})
                    else:
                        return self.write({'status':0, 'data':{'token': ''}, 'msg':'密码错误！'})
                else:
                    return self.write({'status':-1, 'data':{'token': ''}, 'msg':'输入账号不存在！'})
        else:
            return self.write({'status':-1, 'data':{'token': ''}, 'msg':'请输入账号或者密码！'})

class  AddCreawlerHandler(BaseHandler): ##添加爬虫------------------------------------ok
       def post(self):
           name = self.get_argument("name")
           start_urls = self.get_argument("start_urls")
           rules = self.get_argument("rules")
           use_agent_ip_pool = self.get_argument("use_agent_ip_pool")
           cron = self.get_argument("cron")
           isuse = self.get_argument("isuse")
           self.DBAdd(name,start_urls,rules,use_agent_ip_pool,cron,isuse)
       def DBAdd(self,name,start_urls,rules,use_agent_ip_pool,cron,isuse):##判断添加操作
           idnum = r.incrby('generator', 1)
           id = 'crawler:' + str(idnum)
           r.hmset(id, {'Name':name, 'url':start_urls,'rules:':rules,'Use_agent_ip_pool':use_agent_ip_pool,'isuse':isuse,'cron':cron})
           r.rpush('crawler', id)
           return self.write({'status':1,'data':id,'msg':'添加成功！'})

class CrawlersListHandler(BaseHandler): ##爬虫列表-------------------------------ok
        def get(self):
            dir = self.DBGainCrawler()
            s_dumps = json.dumps(dir, sort_keys=True, indent=4, ensure_ascii=False)
            self.write(s_dumps)
        def DBGainCrawler(self):  ##获取爬虫数据
            data = []
            for item in self.list_iter('crawler'):  # 遍历这个列表
                crawlerdata = {'id':item}
                crawlerdata.update(r.hgetall(item))
                data.append(crawlerdata)
            dir= {'status':0,'data':data,'msg':''}
            return dir
        def list_iter(self,name):
            list_count = r.llen(name)
            for index in range(list_count):
                yield r.lindex(name, index)

class  CrawlerHandler(BaseHandler):
        def get(self,Crawlerid):##------------------------爬虫详情ok
            self.DBGainCrawlerDetails(Crawlerid)
        def DBGainCrawlerDetails(self,Crawlerid):  ##获取爬虫详情
            Crawlerid = 'crawler:' + Crawlerid
            data = {'id': Crawlerid}
            data.update(r.hgetall(Crawlerid))
            dir = {'status': 0, 'data': data, 'msg': ''}
            s_dumps = json.dumps(dir, sort_keys=True, indent=4, ensure_ascii=False)
            return self.write(s_dumps)

        def put(self,idnum):##-------------------------------修改爬虫ok
            name = self.get_argument("name")
            start_urls = self.get_argument("start_urls")
            isuse = self.get_argument("IsUse")
            use_agent_ip_pool = self.get_argument("use_agent_ip_pool")
            rules = self.get_argument("rules")
            cron = self.get_argument("cron")
            self.DBUpdate(idnum,name, start_urls,isuse, use_agent_ip_pool, rules, cron)
        def DBUpdate(self,idnum, name, start_urls,isuse, use_agent_ip_pool, rules, cron):  ##判断修改操作
            id = 'crawler:' + str(idnum)
            r.hmset(id, {'Name': name, 'url': start_urls, 'rules:': rules, 'Use_agent_ip_pool': use_agent_ip_pool,'isuse': isuse, 'cron': cron})
            return self.write({'status':0,'msg':'修改成功！'})

        def delete(self, idnum):   ##----------------------删除爬虫 ok
            self.DBDelete(idnum)
        def DBDelete(self, idnum):  ##判断删除操作
            id = 'crawler:' + str(idnum)
            r.delete(id)
            r.lrem("crawler",id)
            return self.write({'status':0,'msg':'删除成功！'})

class TaskListHandler(BaseHandler):  #任务列表
        def get(self):
            Crawlerid = self.get_argument('crawlerid','')
            self.DBGainTask(Crawlerid)
        def DBGainTask(self,Crawlerid): ##获取任务数据
                if len(Crawlerid) > 0:
                    data = []
                    for item in self.list_iter('task'):  # 遍历这个列表
                        if r.hget(item,"CrawlerId") == Crawlerid:
                            taskdata = {'id': item}
                            taskdata.update(r.hgetall(item))
                            data.append(taskdata)
                    dir = {'status': 0, 'data': data, 'msg': ''}
                    s_dumps = json.dumps(dir, sort_keys=True, indent=4, ensure_ascii=False)
                    return self.write(s_dumps)
                else:
                    data = []
                    for item in self.list_iter('task'):  # 遍历这个列表
                        taskdata = {'id': item}
                        taskdata.update(r.hgetall(item))
                        data.append(taskdata)
                    dir = {'status': 0, 'data': data, 'msg': ''}
                    s_dumps = json.dumps(dir, sort_keys=True, indent=4, ensure_ascii=False)
                    return self.write(s_dumps)

        def list_iter(self,name):
            list_count = r.llen(name)
            for index in range(list_count):
                yield r.lindex(name, index)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers={(r"/v1/crawlers", CrawlersListHandler),
                                            (r"/v1/crawler", AddCreawlerHandler),
                                            (r"/v1/acctoun/login", LoginHandler),
                                            (r"/v1/crawler/(\w+)", CrawlerHandler),
                                            (r"/task", TaskListHandler)},
                                  template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()