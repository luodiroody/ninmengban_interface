'''
 AUTH:RODDY
 DATE:2020/2/11
 TIME:10:35
 FILE:readexcel.py
 '''
import openpyxl
class ReadExcel():
    def __init__(self,filename,sheetname):
        self.filename=filename
        self.sheetname=sheetname
    def openfile(self):
        self.workbook=openpyxl.load_workbook(self.filename)
        self.sheet=self.workbook[self.sheetname]
    def read_excel(self):
        self.openfile()
        #调用row,不需要括号
        cases=list(self.sheet.rows)
        #print(cases,type(cases))
        case_list=[]
        for case in cases[1:]:
            case_title=[i.value for i in cases[0]]
            cases_body=[j.value for j in case]
            case_dict=dict(zip(case_title,cases_body))
            case_list.append(case_dict)
        return case_list
    def write_excel(self,row,column,value):
        self.openfile()
        self.sheet.cell(row=row,column=column,value=value)
        self.workbook.save(self.filename)
if __name__=='__main__':
    read=ReadExcel(filename=r'D:\untitled\nimenban_demo\data\apicases_nmb.xlsx',sheetname='register')
    cases=read.read_excel()
    print(cases)