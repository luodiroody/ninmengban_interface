'''
 AUTH:RODDY
 DATE:2020/3/14
 TIME:13:50
 FILE:test_login.py
 '''
import unittest
import os
from common.config import conf
from libray.ddt import ddt,data
from common.readexcel import ReadExcel
from common.dirpath import DATAPATH
from common.handlereplace import ReplaceData
from common.handlrequst import SendRequest
from common.random_str import random_str
from common.radom_email import random_email

@ddt
class TestCount(unittest.TestCase):
    resdexcel=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),
                        sheetname=conf.get('workbook','sheet03'))
    cases=resdexcel.read_excel()
    replace=ReplaceData()
    send=SendRequest()
    def setUp(self):
        """
        执行登录用例前,进行一次注册
        """
        ReplaceData.username =random_str(8)
        ReplaceData.email = random_email()
        register_data='{"username":"#username#","email":"#email#","password":"#username#","password_confirm":"#username#"}'
        register_data=eval(self.replace.replacedata(register_data))
        register_url = 'http://api.keyou.site:8000/user/register/'
        self.send.sendrequest(method='post',url=register_url,json=register_data)
    @data(*cases)
    def testcount(self,case):
        #{"username":"#username#","email":"#email#","password":"#username#","password_confirm":"#username#"}
        #method   url  data  expected  is_num
        method=case['method']
        data=case['data']
        data = self.replace.replacedata(data)
        url = conf.get('env','url')+case['url']
        data=eval(self.replace.replacedata(data))
        res_info=self.send.sendrequest(method=method,url=url,json=data)
        expected=eval(self.replace.replacedata(case['expected']))
        print(res_info.text)
        print('期望结果:{}'.format(expected))
        print('实际结果:{}'.format(res_info.status_code))
    def tearDown(self):
        del ReplaceData.username
        del ReplaceData.email
if __name__=='__main':
    unittest.main()