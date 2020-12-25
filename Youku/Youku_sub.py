import requests
import os
import json
import random
import time
from datetime import datetime
from dateutil import tz
import dateutil.parser
import string
import hashlib


osenviron={}

urllist=[]
hdlist=[]
bdlist=[]




def Av(i,hd,k):
    print('=🔔='*k)
    try:
       headers=eval(hd)
       frm=datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", )
       #print(frm)
       Tm=int(tmstamp(frm)*1000)

       u=i+sam()+str(Tm)
       #print(u)
       response = requests.get(u,headers=headers)
    except Exception as e:
      print(str(e))


def watch(flag,list):
   vip=''
   if flag in osenviron:
      vip = osenviron[flag]
   if flag in os.environ:
      vip = os.environ[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
       exit()
       

def sam():
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(32)]
    random_str = ''.join(str_list)
    m = hashlib.md5()
    m.update(random_str.encode('utf-8'))
    random_str=m.hexdigest()+'&_='
    return random_str



  
def tmstamp(tr):
   tm = dateutil.parser.parse(tr).timestamp()
   return tm

def start():
   global bdlist,urllist,hdlist
   time.sleep(random.randint(1,5))
   watch('sam_newurl',urllist)
   for j in range(8):
     for j in range(7):
       print('====count===='+str(j))
       bdlist=[]
       watch('sam_newheader'+str(j),hdlist)
       if(len(hdlist)==0):
            break
       Av(urllist[0],hdlist[j],(j+1))
       time.sleep(1)
     time.sleep(random.randint(180,200))
   print('🔔'*15)
   
   

if __name__ == '__main__':
       start()
