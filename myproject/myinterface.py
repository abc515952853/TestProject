import requests
import  json  

def test():
    phone = '18506826614'
    mtjid = '888888'
    #生成学员编号
    r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Account')
    mnickname = r.json()

    #发送验证码
    payload = {"phone":phone,"type":1}
    headers = {"Content-Type":"application/json"}  
    r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/SendCode',data = json.dumps(payload),headers = headers) 
    print('发送验证码',r.status_code,r.text)

    #注册
    payload = {"Number": mnickname, "TjNumber": mtjid,"185":phone,"code":"1234"}
    headers = {"Content-Type":"application/json"} 
    r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/Register',data = json.dumps(payload),headers = headers) 
    print('注册',r.status_code,r.text)

    # #登录
    # payload = {"grant_type":'code', "username": mnickname,"password":"123456"}
    # r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Token', data = payload)
    # session = r.json()["token_type"]+" "+r.json()["access_token"]
    # print(r.status_code,r.text)

    # #登录
    # payload = {"grant_type":'code', "username": 'HHX017865',"password":"123456"}
    # r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Token', data = payload)
    # session = r.json()["token_type"]+" "+r.json()["access_token"]
    # print(r.status_code,r.text)

    # #首页
    # headers = {"Content-Type":"application/json","Authorization":session} 
    # r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Home',headers = headers)
    # print(r.status_code,r.json())


    #忘记密码
    # payload = {"phone":"18506826613","code":"1234"}
    # headers = {"Content-Type":"application/json"} 
    # r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/ForgotPassword',data = json.dumps(payload),headers = headers) 
    # print(r.status_code,r.text)

    # payload = {"confrimpwd":"123456"}
    # headers = {"Content-Type":"application/json"}  
    # r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/Confrim',params = payload,headers = headers)
    # print(r.url)
    # print(r.status_code,r.text)

if  __name__ == '__main__':
    test()
