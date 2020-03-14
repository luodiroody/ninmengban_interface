'''
 AUTH:RODDY
 DATE:2020/2/22
 TIME:19:46
 FILE:handlrequst.py
 '''
import requests
class SendRequest():
    def __init__(self):
        self.send=requests.session()
    def sendrequest(self,method,url,headers=None,data=None,json=None,params=None):
        method=method.lower()
        if method == 'post':
            response=requests.post(url=url,headers=headers,data=data,json=json)
        elif method =='get':
            response=requests.get(url=url,headers=headers,params=params)
        elif method =='patch':
            response=requests.patch(url=url,headers=headers,data=data,json=json)
            #global response
        return response

if __name__ == '__main__':
    register_api = r'http://api.keyou.site:8000/keyou1/'
    url = r'http://api.keyou.site:8000/user/tHhkdhh/count'
    send =SendRequest()
    res=send.sendrequest(method='get',url=url).text
    b={"username":"tHhkdhh","count":0}
    if 'username' in res:
        print('zai')
    #res1 =requests.get(url=url,params=None)
    print(res,type(res))

