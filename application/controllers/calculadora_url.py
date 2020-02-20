import web
import app
import json

class Calculadoraurl:
    def GET(self):
        try:
            datos = web.input()
            if datos['token']=="1234":
                numero_1 = int(datos["numero_1"])
                numero_2 = int(datos["numero_2"])
                suma = numero_1 + numero_2
                result = ()
                result['status']="200 ok"
                result['numero_1'] = numero_1
                result['numero_2'] = numero_2
                result['suma'] = suma

                return json.dump(result)
            else:
                result = ()
                result['status']="token no valido"
                return "No te conozco"
        except Exception as e:
            result = ()
            result['status']="faltan valores"
            return "Algo salio mal"