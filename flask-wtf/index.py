from flask import Flask, render_template
app = Flask(__name__)


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
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    params = {'list': list, 'profs': professions}
    return render_template('list_prof.html', **params)



if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")