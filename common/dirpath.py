'''
 AUTH:RODDY
 DATE:2020/2/16
 TIME:15:42
 FILE:dirpath.py
 '''
import os
ABSPATH=os.path.abspath(__file__)
BASEPATH=os.path.dirname(os.path.dirname(ABSPATH))
DATAPATH=os.path.join(BASEPATH,'data')
LOGPATH=os.path.join(BASEPATH,'log')
REPORTPATH=os.path.join(BASEPATH,'report')
TESTCASEPATH=os.path.join(BASEPATH,'testcase')

