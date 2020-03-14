'''
 AUTH:RODDY
 DATE:2020/2/16
 TIME:13:58
 FILE:handlelog.py
 '''
import os
import logging
from common.dirpath import LOGPATH
from common.config import conf
class Mylog():
    @staticmethod
    def mylog():
        #定义log收集器
        mylog=logging.Logger('roody')
        #定义收集器级别
        mylog.setLevel('DEBUG')
        #定义输出文件输出
        fh=logging.FileHandler(filename=os.path.join(LOGPATH,'mylog.log'),encoding='utf8')
        fh.setLevel(conf.get('log','fh'))
        #定义输出到控制台
        fm=logging.StreamHandler()
        fm.setLevel(conf.get('log','fm'))
        #将输出与输入关联
        mylog.addHandler(fh)
        mylog.addHandler(fm)
        #设置输出格式
        formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ff=logging.Formatter(formater)
        fh.setFormatter(ff)
        fm.setFormatter(ff)
        return mylog
my=Mylog()
log=my.mylog()