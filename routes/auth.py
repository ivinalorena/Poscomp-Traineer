from flask import Blueprint, render_template, request, redirect,url_for

auth_bp = Blueprint('auth',__name__,static_folder='static',template_folder='templates')

@auth_bp.route('/', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        # pegar os dados do formulario
        user = request.form['user'] 
        senha = request.form['pwd'] 
        return redirect(url_for('user.dash'))
    
    return '''
<form method="POST">
    Usuário: <input type='text' name = 'user' /> </br>
    Senha: <input type = 'password' name='pwd'/> <br/>
    <input type='submit' value='entrar'/>
</form>
'''