'''
 AUTH:RODDY
 DATE:2020/3/11
 TIME:12:01
 FILE:radom_email.py
 '''
import  random
def random_email():
    tel =str(random.randint(100000000,9999999999))[0:8]
    tel='135'+tel
    email=tel+'@163.com'
    return email
#print(email())