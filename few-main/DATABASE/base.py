import sqlite3
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/')
def form():
    return render_template("index.html")

@app.route('/second')
def two():
    return render_template("two.html")


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        login_user = request.form['login']
        password_user = request.form['password']

        with sqlite3.connect('baza.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            user = cursor.execute('SELECT * FROM users WHERE name = ? AND password = ?',(login_user,password_user)).fetchone()

            if user is not None:
                return home()
            else:
                return "Не правильний логін або пароль"+form()










if __name__ == '__main__':
    app.run(debug = True)

    
#conn = sqlite3.connect("baza.db")
#cursor = conn.cursor()

#login = input("Введіть логін ")
#
#cursor.execute(f"SELECT name FROM users WHERE name=='{login}'")
#data = cursor.fetchall()
#print("Ваші логіни співпадають")



#@app.route('/')
#def home():
#    return render_template("index.html")
#
#@app.route('/two')
#def two():
#    return render_template("two.html")







