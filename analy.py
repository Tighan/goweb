import pickle
def top10():
    with open('/home/tig/gpweb/gpcountlist.pkl','rb') as f:
        li=pickle.load(f)
    ll=[]#dict 's total  list
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    di={}
    for i in li:
         ll.append(eval(i[0]))
         di.update(eval(i[0]))
    for q in ll:
        for z in q.keys():
                l3.append(z)
    l1=list(set(l3))
    for i in l1:
        count=l3.count(i)
        l2.append(str(count)+i)
    l2.sort(reverse=True)
    l6=l2[0:10]
    for s in l6:
        l4.append(s[1:])
    
    return l4[0:10]
top10()