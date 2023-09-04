from flask import Flask, render_template, url_for, request, abort, flash, redirect, session, make_response
from werkzeug.utils import secure_filename
from pathlib import PurePath, Path

app = Flask(__name__)

app.secret_key = '6f696cdfa258e29c251ff55fc06d79650a25f19941fa2f8662a0bc1847c634af'


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        response = make_response(render_template('base.html', **{'name': request.form.get('username')}))
        response.set_cookie('username', request.form.get('username'))
        # не знал сессию или куки, сделал и то и другое

        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email')
        return response
    return render_template('input_lg_and_pwd.html')

@app.route('/main/')
def main():
    return render_template('base.html', **{'name': request.cookies.get('username')})


@app.route('/exit/')
def exit():
    session.pop('username', None)
    session.pop('email', None)
    res = make_response(render_template('input_lg_and_pwd.html'))
    res.set_cookie('username','', expires=0)
    return res


@app.route('/fruits/')
def fruits():
    _fr = ["банан марсианский", "персик с галактики персиков", "яблоко солнечное", "маракуя плутоная"]
    context = {'fr': _fr}
    return render_template('fruits.html', **context)


@app.route('/vegetable/')
def vegetable():
    _vt = ["огурец с земли", "помидор далекий", "баклажан идеальный"]
    context = {'vt': _vt}
    return render_template('vegetables.html', **context)


@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')


if __name__ == '__main__':
    app.run()


























@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':

        response = make_response(render_template('base.html', **{'name': request.form.get('username')}))
        response.set_cookie('username', request.form.get('username'))

        session['username'] = request.form.get('username')
        session['email'] = request.form.get('email')
        return response

    return render_template('input_lg_and_pwd.html')

@app.route('/main/')
def main():
    return render_template('base.html', **{'name': session['username']})


@app.route('/exit/')
def exit():
    session.pop('username', None)
    session.pop('email', None)
    return


@app.route('/fruits/')
def fruits():
    _fr = ["банан марсианский", "персик с галактики персиков", "яблоко солнечное", "маракуя плутоная"]
    context = {'fr': _fr}
    return render_template('fruits.html', **context)


@app.route('/vegetable/')
def vegetable():
    _vt = ["огурец с земли", "помидор далекий", "баклажан идеальный"]
    context = {'vt': _vt}
    return render_template('vegetables.html', **context)


@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')




if __name__ == '__main__':
    app.run()
