import httplib2,json
def get_falist():
    h=httplib2.Http()
    head={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
    'Cookie':'s=iaksux2b.17old1a; xq_a_token=303136ef30dbca9e862eb6c257cfd7cc1677811a; xq_r_token=336fb50505d06350443ef4773c54da4da7d24808; __utma=1.1503889104.1433580574.1433580574.1433589003.2; __utmz=1.1433580574.1.1.utmcsr=sogou|utmccn=(organic)|utmcmd=organic|utmctr=%E9%9B%AA%E7%90%83; Hm_lvt_1db88642e346389874251b5a1eded6e3=1433580574; xqat=303136ef30dbca9e862eb6c257cfd7cc1677811a; xq_is_login=1; xq_token_expire=Wed%20Jul%2001%202015%2016%3A49%3A49%20GMT%2B0800%20(CST); bid=bfd5804260933ce18135f8e7cbb98f57_iaksvakp; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1433589003; __utmb=1.1.10.1433589003; __utmc=1; __utmt=1'}
    url='http://xueqiu.com/cubes/discover/rank/cube/list.json?category=14&page=1&count=10000'
    resp,cont=h.request(url,headers=head)
    f=json.loads(cont)
    total=f['list']
    list=[]
    for each in total:
        list.append(each['symbol'])
    return list
get_falist()
