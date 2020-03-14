'''
 AUTH:RODDY
 DATE:2020/3/8
 TIME:14:13
 FILE:handlemail.py
 '''
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from common.config import conf
from common.dirpath import REPORTPATH
#连接smpt服务
def sendemai(filename,title):
        smtp = smtplib.SMTP_SSL(host=conf.get('email','host'),port=conf.getint('email','port'))
        smtp.login(user=conf.get('email','user'),password=conf.get('email','password'))
        #创建一个组件
        msg=MIMEMultipart()
        #第二步构建一个邮件
        with open(os.path.join(REPORTPATH,filename),'rb') as f :
            content=f.read()
        #创建邮件文本内容
        text_msg=MIMEText(content,_subtype='html',_charset='utf8')
        #添加到多组件的邮件中
        msg.attach(text_msg)
        #创建附件
        report_msg=MIMEApplication(content)
        report_msg.add_header('content-disposition', 'attachment', filename=filename)
        #将附件添加到多组件的邮件中
        msg.attach(report_msg)
        #主题
        msg['Subject']=title
        #发件人
        msg['From']='244369101@qq.com'
        #收件人
        msg['To']='244369101@qq.com'
        #第三步发送邮件
        smtp.send_message(msg,from_addr=conf.get('email','from_addr'),
                          to_addrs=eval(conf.get('email','to_addrs')))
#sendemai('result.html','测试报告')