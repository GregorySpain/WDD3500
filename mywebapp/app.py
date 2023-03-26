from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/admin')
def admin_page():
    return 'Welcome to the admin page'


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect('/admin')
    else:
        return redirect('/guest/%s' % name)


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


if __name__ == '__main__':
    app.run()