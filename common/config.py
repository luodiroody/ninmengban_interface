'''
 AUTH:RODDY
 DATE:2020/2/11
 TIME:20:08
 FILE:configparser.py
 '''
import configparser
import os
from common.dirpath import DATAPATH
class Config (configparser.ConfigParser):
    def __init__(self,filename):
        self.filename=filename
        super().__init__()
        super().read(self.filename)
    def write_data(self,section,option,value):
        self.set(section=section,option=option,value=value)
        self.write(fp=open(self.filename,'w',encoding='utf8'))
conf=Config(filename=os.path.join(DATAPATH,'conf.ini'))
# print(type(conf.get('workbook','name')))
# print(conf.get('workbook','sheet01'))
# print(conf.get('log','formater'))