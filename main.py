from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/promedionotas', methods=['GET', 'POST'])
def promedionotas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1+nota2+nota3) / 3
        if promedio >= 40:
            if asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"
        else:
            estado = "Reprobado"
        return render_template('promedionotas.html', promedio=promedio, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia, estado=estado)
    return render_template('promedionotas.html')

@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    if request.method == 'POST':
        resultado= ''
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        if len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            mensaje =  'El nombre con mayor cantidad de caracteres es: ' + nombre1
            mensaje2 = 'El nombre tiene: ' + str(len(nombre1)) + ' caracteres'
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            mensaje = 'El nombre con mayor cantidad de caracteres es: ' + nombre2
            mensaje2 = 'El nombre tiene: ' +  str(len(nombre2)) + ' caracteres'
        elif len(nombre3) > len(nombre1) and len(nombre3) > len(nombre2):
            mensaje = 'El nombre con mayor cantidad de caracteres es: ' + nombre3
            mensaje2 = 'El nombre tiene: ' +  str(len(nombre1)) + ' caracteres'
        else:
            mensaje = 'Los nombres tienen la misma cantidad de caracteres.'
            mensaje2 = ''
        return render_template('nombres.html', mensaje=mensaje, mensaje2=mensaje2)
    return render_template('nombres.html')

if __name__ == '__main__':
    app.run(debug=True)