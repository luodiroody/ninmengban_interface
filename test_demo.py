'''
 AUTH:RODDY
 DATE:2020/3/11
 TIME:10:28
 FILE:test_demo.py
 '''
class Abb():
    def Pru(self):
        print('22222')
Abb.dds='this is '
print(getattr(Abb,'dds'))
del Abb.dds
print(getattr(Abb,'dds'))