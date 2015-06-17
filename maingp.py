import sqlite3
from eachpagefor_gp import rethegp
from down_list import get_falist
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

