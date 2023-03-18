from flask import Flask, render_template

app = Flask(__name__)
HOST = '127.0.0.1'


@app.route('/')
def main_web_page():
    return render_template('MainWebPage.html', host_url='http://127.0.0.1:5000')


@app.route('/aboba')
def aboba_page():
    return render_template('aboba.html', host_url='http://127.0.0.1:5000')


if __name__ == '__main__':
    app.run(host=HOST)
