from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('telainicial.html')

@app.route('/POSCOMP2022')
def POSCOMP2022():
    return render_template('POSCOMP2022.html')

@app.route('/POSCOMP2023')
def POSCOMP2023():
    return render_template('POSCOMP2023.html')

@app.route('/POSCOMP2024')
def POSCOMP2024():
    return render_template('POSCOMP2024.html')

@app.route('/POSCOMP2019')
def POSCOMP2019():
    return render_template('POSCOMP2019.html')

@app.route('/POSCOMP2020')
def POSCOMP2020():
    return render_template('POSCOMP2020.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')
#@app.route('/POSCOMP2023')
#def POSCOMP2023():
#    return render_template('POSCOMP2023.html')

if __name__ == '__main__':
    app.run()