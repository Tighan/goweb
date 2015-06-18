import web
from analy import top10
from maingp import start
start()
topkeys,dict=top10()
render=web.template.render('templates/')
db=web.database(dbn='sqlite',db='gpdata.db')
urls=(
    '/','index')
class index:
    """docstring for index"""
    def GET(self):
        falist=db.select('gp')
        return render.index(falist,topkeys,dict)
if __name__ == '__main__':
         app=web.application(urls,globals())    
         app.run() 