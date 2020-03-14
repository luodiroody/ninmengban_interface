'''
 AUTH:RODDY
 DATE:2020/2/25
 TIME:20:40
 FILE:handlemysql.py
 '''
import pymysql
from common.config import conf
class Connet():
    def __init__(self):
        self.host=conf.get('mysql','host')
        self.port= conf.getint('mysql','port')
        self.user=conf.get('mysql','user')
        self.password=conf.get('mysql','password')
        self.charset=conf.get('mysql','charset')
        self.connot=pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    charset=self.charset,
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.cursor=self.connot.cursor()
    def select_data(self,sql):
        self.connot.commit()
        res=self.cursor.execute(sql)
        res1=self.cursor.fetchall()[0]
        return res1
    def close(self):
        self.connot.commit()
        self.cursor.close()
        self.connot.close()

if __name__ =='__main__':
    connet=Connet()
    sql='select leave_amount from futureloan.member WHERE  mobile_phone = 13367899876'
    res=connet.select_data(sql)
    print(res['leave_amount'])



#cursorclass=pymysql.cursors.DictCursor,
