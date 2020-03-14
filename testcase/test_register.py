'''
 AUTH:RODDY
 DATE:2020/3/11
 TIME:9:36
 FILE:test_register.py
 '''
import os
import  unittest
from common.readexcel import ReadExcel
from common.config import conf
from libray.ddt import ddt,data
from common.radom_email import random_email
from common.random_str import random_str
from common.handlereplace import ReplaceData
from common.handlrequst import SendRequest
from common.dirpath import DATAPATH
from common.handlelog import log

@ddt
class TestRegister(unittest.TestCase):
    resdexcel=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),
                        sheetname=conf.get('workbook','sheet01'))
    cases=resdexcel.read_excel()
    replace=ReplaceData()
    send=SendRequest()
    @data(*cases)
    def test_register(self,case):
        #{"username":"#username#","email":"#email#","password":"#username#","password_confirm":"#username#"}
        #method   url  data  expected  is_num
        method=case['method']
        url=conf.get('env','url')+case['url']
        expected=eval(case['expected'])
        ReplaceData.username=random_str(case['is_num'])
        ReplaceData.email=random_email()
        data=case['data']
        data=eval(self.replace.replacedata(data))
        #print(data)
        res_info=self.send.sendrequest(method=method,url=url,json=data).json()
        #print(res_info)
        try :
            print('预期结果:{}'.format(expected))
            print('实际结果:{}'.format(res_info))
            if case['case_id'] < 3:
                self.assert_dict_in(expected,res_info)
            else:
                self.assert_dict_notin(expected,res_info)
            print('用例:{}通过'.format(case['title']))
        except AssertionError as e:
            raise e
            print('用例:{}未通过'.format(case['title']))
    def assert_dict_in(self,dict1,dict2):
        '''
        :param dict1:预期结果
        :param dict2:实际结果
        :return:
        '''
        key=list(dict2.keys())
        print('实际结果中的key:',key)
        for i in dict1:
            print('预期结果中的key;',i)
            if i in key :
                pass
            else:
                raise AssertionError("{} not in {}".format(dict1,dict2))
    def assert_dict_notin(self,dict1,dict2):
        '''
        :param dict1:预期结果
        :param dict2:实际结果
        :return:
        '''
        key=list(dict2.keys())
        print('实际结果中的key:',key)
        for i in dict1:
            print('预期结果中的key;',i)
            if i not in key :
                pass
            else:
                raise AssertionError("{} in {}".format(dict1,dict2))

if __name__=='__main__':
    unittest.main()





