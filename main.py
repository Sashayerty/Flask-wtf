from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def our_mission(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def proffesion(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def lists(list):
    profs = ['Программист', 'Повар', 'Врач']
    return render_template('lists.html', listtype=list, list=profs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
