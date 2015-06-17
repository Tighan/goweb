import sqlite3
import pickle
c=[]
cx=sqlite3.connect('/home/tig/gpweb/gpdata.db')
cu=cx.cursor()
cu.execute("select fina from gp")
f=cu.fetchall()
dels=(u'',)
l=[i for i in f if i != (u'',)]
with open('/home/tig/gpweb/gpcountlist.pkl','wb') as f:
    pickle.dump(l,f)
    
