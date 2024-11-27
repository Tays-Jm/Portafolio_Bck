from flask import Flask, render_template, redirect,url_for,request

app = Flask(__name__)
usuario = {
    'email': 'ejemplo@gmail.com',
    'password': '123456'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/proyectos')
def proyectos():
    return render_template('Proyectos.html')

@app.route('/primera')
def primerpag():
    return render_template('otro.html')

@app.route('/Documentacion')
def documentacion():
    return render_template('Documentacion.html')


@app.route('/Codigo')
def codigo():
    return render_template('Editor.html')


@app.route('/Stackoverflow')
def Presentacion():
    return render_template('Stackoverflow.html')

@app.route('/Lenguajes')
def Lenguajes():
    return render_template('Lenguajes.html')

@app.route('/Redes')
def Redes():
    return render_template('Contacto.html')

@app.route('/Login')
def login(): 
    return render_template('login.html')


@app.route('/Modeva')
def modeva():
    return render_template('Modeva.html')
@app.route('/Inteligencia')
def inteligencia():
    return render_template('Ai.html')

@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    password = request.form['password']
    print(email, password)
    if email == usuario['email'] and password == usuario['password']:
        return render_template('success.html')
    else:
        print("Llegale >:(")
        return redirect(url_for('home'))


if __name__=='__main__':
    app.run(debug=True)
