'''
 AUTH:RODDY
 DATE:2020/3/11
 TIME:11:51
 FILE:random_str.py
 '''
import random

import string
def random_str(number):
    number=int(number)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, number))
    return  ran_str