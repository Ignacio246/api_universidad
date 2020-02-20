import web
import app
import csv

class archivos_csv:
    def GET(self):
        try:
            datos = web.input()
            if datos['token']=="1234":
                numero_1 = int(datos["numero_1"])
                numero_2 = int(datos["numero_2"])
                suma = numero_1 + numero_2
                result = []
                result.append(numero_1)
                result.append(numero_2)
                result.append(suma)

                with open('staic/csv/datos.csv','a+', newlines='') as csvfile:
                    writer=csv.writer(csvfile)
                    writer=writerow(result)
                
                result="numero_1,numero_2,suma/n"
                with open('static/csv/datos.csv','r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        fila =str(row['numero_1'])+","+str(row['numero_2'])+","+str(row['suma'])
                        result+=fila "\n"
                    return result

                return json.dump(result)
            else:
                result = ()
                result['status']="token no valido"
                return "No te conozco"
        except Exception as e:
            result = ()
            result['status']="faltan valores"
            return "Algo salio mal"