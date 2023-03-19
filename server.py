from flask import Flask, render_template, redirect

from data.db_session import global_init, create_session
from data.login_form import LoginForm

app = Flask(__name__)
HOST = '127.0.0.1'
server_url = 'http://127.0.0.1:5000/'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def first_web_page():
    return redirect(f'{server_url}ru')


@app.route('/<language>')
def main_web_page(language):
    return render_template(f'main_page_{language}.html', host_url=f'{server_url}{language}', language=language,
                           domen='')


@app.route('/<language>/login', methods=['GET', 'POST'])
def login_form(language):
    form = LoginForm()
    if form.validate_on_submit():
        return 'OK'
    return render_template(f'login_form_{language}.html', host_url=f'{server_url}{language}', language=language,
                           domen='/login', form=form)


@app.route('/<language>/aboba')
def aboba_page(language):
    return render_template(f'aboba_{language}.html', host_url=f'{server_url}{language}', domen='/aboba',
                           language=language)


@app.route('/switch_language/<new_lang>')
def switch_language(language):
    pass


if __name__ == '__main__':
    app.run(host=HOST)
    global_init('db/OnlineDeveloperSchool.db')
    session = create_session()
