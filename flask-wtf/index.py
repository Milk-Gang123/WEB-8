from flask import Flask, render_template, request

app = Flask(__name__)

FORM_DATA = {'surname': 'Watny', 'name': 'Mark', 'edu': 'выше среднего', 'prof': ['штурман марсохода'],
             'gender': 'male', 'motiv': 'Всегда мечтал застрять а Марсе!', 'ready': 'True'}
PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
MEMBERS  = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Биф']


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    params = {'title': title}
    return render_template('base.html', **params)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        prof = 'True'
    else:
        prof = 'False'
    params = {'prof': prof}
    return render_template('training.html', **params)


@app.route('/list_prof/<list>')
def list_prof(list):
    params = {'list': list, 'profs': PROFESSIONS}
    return render_template('list_prof.html', **params)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def show_form():
    global FORM_DATA
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        FORM_DATA["surname"] = request.form['surname']
        FORM_DATA["name"] = request.form['name']
        #FORM_DATA["email"] = request.form['email']
        FORM_DATA["edu"] = request.form['class']
        profs = []
        for i in range(1, 16):
            try:
                a = request.form[f'prof{i}']
                profs.append(a)
            except Exception:
                pass
        FORM_DATA["prof"] = profs
        FORM_DATA["gender"] = request.form['sex']
        FORM_DATA["motiv"] = request.form['about']
        a = request.form['accept']
        if a == 'on':
            FORM_DATA["ready"] = 'True'
        else:
            FORM_DATA["ready"] = 'False'
        print(FORM_DATA)
        return "Форма отправлена"


@app.route('/answer')
@app.route('/auto_answer')
def show_answer():
    params = FORM_DATA
    params['prof'] = ', '.join(params['prof'])
    return render_template('auto_answer.html', **params)


@app.route('/login', methods=['POST', 'GET'])
def show_login_form():
    params = {'title': 'Аварийный доступ'}
    if request.method == 'GET':
        return render_template('login.html', **params)
    elif request.method == 'POST':
        return "Доступ получен"


@app.route('/distribution')
def show_dist():
    params = {'members': MEMBERS}
    return render_template('distribution.html', **params)


@app.route('/table/<gender>/<int:age>')
def show_table(gender, age):
    params = {'gender': gender, 'age': age}
    return render_template('table.html', **params)



if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")