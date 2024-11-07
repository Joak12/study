from flask import Flask, render_template, redirect, url_for, request, Blueprint
from .controllers import user_controller
from .controllers import tarefa_controller

app = Flask(__name__)
app.register_blueprint(user_controller.bp)

@app.route('/')
def login():
    return render_template('/users/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Processar o formulário de cadastro
        # ...
        return redirect(url_for('login'))
    return render_template('/users/register.html')

if __name__ == '__main__':
    app.run(debug=True)