from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Это главная страница.'

@app.route('/blog')
def blog():
    return 'Это блог с заметками о работе и увлечениях.'

@app.route('/user/<username>')
def user_profile(username):
    return f"Это профиль пользователя {username}"

@app.route('/user/<int:user_id>')
def user_ID(user_id):
    return f"Это профиль пользователя с ID {user_id}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        return render_template('about.html')
    else:
        return render_template('login.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)