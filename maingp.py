import sqlite3
from eachpagefor_gp import rethegp
from down_list import get_falist
import pickle
cx=sqlite3.connect('/home/tig/gpweb/gpdata.db')
try:
    cx.execute('drop table gp')
    cx.execute('create table gp(urlid,fina,per,userid,username)')
except:
    cx.execute('create table gp(urlid,fina,per,userid,username)')
gplist=get_falist()
for i in gplist:
    sql=rethegp(i)
    cx.execute("insert into gp values (?,?,?,?,?)", sql)
    cx.commit()
c=[]
cx1=sqlite3.connect('/home/tig/gpweb/gpdata.db')
cu1=cx1.cursor()
cu1.execute("select fina from gp")
f=cu1.fetchall()
dels=(u'',)
l=[i for i in f if i != (u'',)]
with open('/home/tig/gpweb/gpcountlist.pkl','wb') as f:
    pickle.dump(l,f)
    
