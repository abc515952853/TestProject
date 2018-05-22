# import redis
# import time
#
# from croniter import croniter
# from datetime import datetime
# import json
# from date2cron import date_to_cron
#
# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
# r = redis.Redis(connection_pool=pool)
#
#
#
# # base = datetime(2010, 1, 25, 4, 46)
# # iter = croniter('*/5 * * * *', base)  # every 5 minutes
# # print(iter)
# #
# # # def list_iter(name):
# # #     list_count = r.llen(name)
# # #     for index in range(list_count):
# # #         yield r.lindex(name, index)
# # #
# # # Crawlerlist=[]
# # # for item in list_iter('CrawlerList'): # 遍历这个列表
# # #     Crawlerlist.append(r.hgetall(item))
# # # print(Crawlerlist)
# # # # 使用
# # #
# # #
# # # idnum = r.incrby('generator', 1)
# # # print (type(idnum))
# # # id = 'crawler:' + str(idnum)
# # # r.hmset(id, {'Name':'111', 'url':'111','rules:':'11','Use_agent_ip_pool':'111','IsUse':111,'cron':'111'})
# # # r.rpush('crawler',id)
# #
# # #
# # # r.hdel("crawler:6",'Name','url','Use_agent_ip_pool','IsUse','cron')    # 删除一个键值对
# # # r.delete("crawler:6")    # 删除一个键值对
# # def list_iter(name):
# #     list_count = r.llen(name)
# #     for index in range(list_count):
# #         yield r.lindex(name, index)
# #
# #
# # data = []
# # for item in list_iter('task'):  # 遍历这个列表
# #     if r.hget(item, "CrawlerId")=='crawler:3':
# #         taskdata = {'id': item}
# #         taskdata.update(r.hgetall(item))
# #         data.append(taskdata)
# # dir = {'status': 0, 'data': data, 'msg': ''}
# # print(dir)
#
# dict = {"asdf": "我们的python学习"}
# json.dumps(dict,encoding="UTF-8",ensure_ascii=False)
# print (dict)
#
#

#!/usr/bin/python
# import json
#
# data =b'{"session_key":"yZZd6dNn937a+dk42+ChPA==","openid":"ohVwU0cP-V9kFzP62fWYZXhix__8"}'
#
# json = json.loads(data)
# print(json)

# from datetime import datetime, timedelta
# expiretime=datetime.now()+timedelta(days=7)
# print (expiretime)
# print (expiretime.strftime)


#!/usr/bin/python3

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))