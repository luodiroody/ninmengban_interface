'''
 AUTH:RODDY
 DATE:2020/3/12
 TIME:11:00
 FILE:test_count.py
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


@ddt
class TestCount(unittest.TestCase):
    resdexcel=ReadExcel(filename=os.path.join(DATAPATH,conf.get('workbook','name')),
                        sheetname=conf.get('workbook','sheet02'))
    cases=resdexcel.read_excel()
    replace=ReplaceData()
    send=SendRequest()
    @data(*cases)
    def testcount(self,case):
        #{"username":"#username#","email":"#email#","password":"#username#","password_confirm":"#username#"}
        #method   url  data  expected  is_num
        method=case['method']
        data=case['data']
        is_num = case['is_num']
        print(is_num)
        if case['is_num']:
            ReplaceData.username =random_str(case['is_num'])
            print(ReplaceData.username)
        else:
            ReplaceData.username=getattr(ReplaceData,'username')
        data = self.replace.replacedata(data)
        url = conf.get('env','url')+data
        #data=eval(self.replace.replacedata(data))
        expected=eval(self.replace.replacedata(case['expected']))
        res_info=self.send.sendrequest(method=method,url=url).text
        try:
            print('期望结果:{}'.format(expected))
            print('实际结果:{}'.format(res_info))
            if case['case_id'] < 3:
                self.assert_str_in(expected,res_info)
            else:
                self.assert_str_notin(expected,res_info)
            print('用例{}测试通过'.format(case['title']))
        except AssertionError as e:
            raise e
            print('用例{}测试未通过'.format(case['title']))
    def assert_str_in(self,dict1,res_str):
        '''
        :param dict1:预期结果
        :param res_str:实际结果
        :return:
        '''
        key=list(dict1.keys())
        print('实际结果中的key:',key)
        for i in key :
            if i not in res_str:
                raise AssertionError
            else :
                pass
    def assert_str_notin(self,dict1,res_str):
        '''
        :param dict1:预期结果
        :param res_str:实际结果
        :return:
        '''
        key=list(dict1.keys())
        print('实际结果中的key:',key)
        for i in key :
            if i in res_str:
                raise AssertionError
            else :
                pass

if __name__ == '__main__':
    unittest.main()

