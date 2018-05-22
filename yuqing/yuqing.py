import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path

import hashlib  ##MD5加密
import DB


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class LoginHandler(tornado.web.RequestHandler):
    def Post(self):
        username = 'shenbin523'##self.get_argument("username")
        password = '123456'##self.get_argument("password")
        if username and password:
            dbusername=dbsession.query(DB.employee).filter_by(username=username).all()
            if dbusername:
                dbpassword = dbsession.query(DB.employee,password).filter_by(username=username).all()
                passwordmd5 = hashlib.md5()
                passwordmd5.update(password.encode(encoding='utf-8'))
                print (dbpassword)
                print (passwordmd5)
                print (password)
                if dbpassword == passwordmd5:
                    return self.write({'status': 0, 'data': {'token': ''}, 'msg': '登录成功！'})
                else:
                    return self.write({'status': -1, 'data': {'token': ''}, 'msg': '密码错误！'})
            else:
                return self.write({'status': -1, 'data': {'token': ''}, 'msg': '账号不存在！'})
        else:
            return self.write({'status':-1, 'data':{'token': ''}, 'msg':'请输入账号或者密码！'})

if __name__ == "__main__":
    DB.Base.metadata.create_all(DB.engine) ###数据库连接
    DB.Session = DB.sessionmaker(bind=DB.engine)
    dbsession = DB.Session()

    tornado.options.parse_command_line()   ###TORNADO启动
    app = tornado.web.Application(handlers={(r"/v1/account/login", LoginHandler)},
                                  template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()