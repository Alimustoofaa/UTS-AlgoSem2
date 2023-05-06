import re
from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$'
    return bool(re.match(pattern, password))


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', data={})
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = {}
        if len(username) == 0:
            message['username'] = 'Username is required'
        else:
            message['username'] = 'Username valid'
        if len(password) == 0:
            message['password'] = 'Password is required'
        else:
            message['password'] = 'Password valid'
        
        if not validate_password(password):
            message['validate_password'] = 'Invalid password. Password must be at least 6 characters long and contain a combination of letters and numbers.'
        else:
            message['validate_password'] = 'Password valid'
        return render_template('index.html', data=message)
    
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', data={})
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_conf = request.form['confirmpassword']
        message = {}
        # validation
        if len(username) == 0:
            message['username'] = 'Username is required'
        else:
            message['username'] = 'Username valid'

        if len(password) == 0:
            message['password'] = 'Password is required'
        else:
            message['password'] = 'Password valid'

        if len(password_conf) == 0:
            message['confirmpassword'] = 'Password Confirmasi is required'
        else:
            message['confirmpassword'] = 'Password Confirmasi valid'

        if not validate_password(password):
            message['validate_password'] = 'Invalid password. Password must be at least 6 characters long and contain a combination of letters and numbers.'
        else:
            message['validate_password'] = 'Password valid'

        if not validate_password(password_conf):
            message['validate_confirmpassword'] = 'Invalid password. Password must be at least 6 characters long and contain a combination of letters and numbers.'
        else:
            message['validate_confirmpassword'] = 'Password valid'

        if not password == password_conf:
            message['match_password'] = 'Password and Confirmasi password not match'
        else:
            message['match_password'] = 'Password and Confirmasi is matched'
        
        print(request.form['password'])
        return render_template('register.html', data=message)

run_with_ngrok(app)
app.run()