from flask import Flask, request, render_template, redirect
from model.models import Artist, Album, Song, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)

@app.route('/tasks')
def task():
    tasks = ("Сьесть кота", "Нарезать детей", "Посмотреть рикролл", "Прийти ночью домой к тем, кто посмотрел эти задания и не выполнил их")
    return render_template('tasks.html', tasks=tasks*len(tasks))

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
        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    else:
        return render_template('login.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/songs')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)

bigchars = "QWERTYUIOPASDFGHJKLZXCVBNMЙЦЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"

@app.route('/game', methods=['GET', 'POST'])
def passwordgame():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username.lower() not in password.lower():
            return render_template('login.html', error="Пароль должен содержать логин")

        check = False
        for i in bigchars:
            if i in password:
                check = True
        if not check:
            return render_template('login.html', error="Пароль должен содержать большие буквы")

        check = False
        for i in bigchars.lower():
            if i in password:
                check = True
        if not check:
            return render_template('login.html', error="Пароль должен содержать маленькие буквы")

        check = False
        for i in bigchars.lower():
            if i in password:
                check = True
        if not check:
            return render_template('login.html', error="Пароль должен содержать маленькие буквы")

        return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    else:
        return render_template('login.html', error="")

if __name__ == '__main__':
    app.run(port=8000, debug=True)