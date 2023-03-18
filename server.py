from flask import Flask, render_template, redirect

app = Flask(__name__)
HOST = '127.0.0.1'


@app.route('/')
def main_web_page():
    return redirect("http://127.0.0.1:5000/ru")


@app.route('/en')
def main_web_page_en():
    return render_template('main_page_en.html', host_url='http://127.0.0.1:5000/en', language='en', domen='')


@app.route('/ru')
def main_web_page_ru():
    return render_template('main_page_ru.html', host_url='http://127.0.0.1:5000/ru', language='ru', domen='')


@app.route('/<language>/aboba')
def aboba_page(language):
    return render_template(f'aboba_{language}.html', host_url=f'http://127.0.0.1:5000/{language}', domen='/aboba',
                           language=language)


@app.route('/switch_language/<new_lang>')
def switch_language(language):
    pass


if __name__ == '__main__':
    app.run(host=HOST)
