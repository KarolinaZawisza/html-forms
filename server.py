from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def receive_data():
    login = request.form['login']
    password = request.form['password']
    return render_template('login.html', login=login, password=password)


if __name__ == '__main__':
    app.run(debug=True)