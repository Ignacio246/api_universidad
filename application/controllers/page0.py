import web
import app

render = web.template.render('application/views')
class Page0:
    def GET(self):
        name = "Ignacio"
        number1 = 10
        number2 = 15
        return render.page0(name,number1,number2)
