import web
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append ('Constant')

urls = (
    '/page0/?', 'application.controllers.page0.page0',
    '/page1/?', 'application.controllers.page1.Page1',
    '/page2/?', 'application.controllers.page2.Page2',
    '/calculadora_url/?', 'application.controllers.calculadora_url.Calculadoraurl',
    '/archivos_csv/?','application.controllers.archivos.csv.archivos_csv',
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = False
    app.run()