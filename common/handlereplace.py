'''
 AUTH:RODDY
 DATE:2020/2/29
 TIME:14:49
 FILE:handlereplace.py
 '''
import  re
from common.config import conf
class ReplaceData():
    pattern = r'#(\w*)#'
    def replacedata(self,strs):
        while re.search(pattern=self.pattern,string=strs):
            res=re.search(r'#(\w*)#',strs)
            res2=res.group(1)
            try :
                value=conf.get('env',res2)
            except:
                value=str(getattr(ReplaceData,res2))
            finally:
                strs=strs.replace(res.group(),value)
        return strs
if __name__ =='__main__':
    s1= '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
    s2= '{"member_id":member_id,"title":1,"amount":6300.00,"loan_rate":"12.0","loan_term":12,"loan_date_type":1,"bidding_days":1}'
    rep=ReplaceData()
    ReplaceData.member_id=999999999
    resp1=rep.replacedata(s1)
    resp2=rep.replacedata(s2)
    print(resp1)
    print(resp2,type(resp2))

