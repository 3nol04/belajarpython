from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fakultas')
def fakultas():    
    fakultas = ["FIKR","FEB"]
    return render_template('fakultas.html',fakultas=fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
        {
        'nama' : "Teknik Informatika",
        "falkutas" : "FIKR"
        },{
        'nama' : "Sistem Informasi",
        "falkutas" : "FIKR"
        }
        ,{
        'nama' : "Akuntansi",
        "falkutas" : "FEB"
        }
    ]
    return render_template('prodi.html',prodi=prodi)
@app.route('/contect')
def contect():
    return render_template('contect.html')


if __name__ =='__main__':
    app.run(debug=True)