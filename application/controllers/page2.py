import web
import app

render = web.template.render('application/views')
class Page2:
    def POST(self):
        return render.page2()
    def POST(self):
        formu=web.input()
        number1 = int(formu["number1"])
        number2 = int(formu["number2"]) 
        add = number1 +number2