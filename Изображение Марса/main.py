from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def show_mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def show_slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def show_advert():
    return '''<p>Человечество вырастает из детства.</p>
              <p>Человечеству мала одна планета.</p>
              <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
              <p>И начнем с Марса!</p>
              <p>Присоединяйся!</p>'''


@app.route('/image_mars')
def show_image():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" type="text/css"
                        href="{url_for('static', filename="css/style.css")}">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                <h1>Жди нас, Марс!<h1>
                <img src="{url_for('static', filename='/img/mars.jpg')}">
                <p>Вот она какая, красная планета.</p>
                </body>
                </html>'''


@app.route('/promotion_image')
def show_promotion_image():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <link rel="stylesheet" type="text/css"
                        href="{url_for('static', filename="css/style.css")}">
                    <!-- Bootstrap CSS -->
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                </head>
                <body>
                <h1>Жди нас, Марс!<h1>
                <img src="{url_for('static', filename='/img/mars.jpg')}">
                <div class="alert alert-primary" role="alert">
                  Человечество вырастает из детства.
                </div>
                <div class="alert alert-secondary" role="alert">
                  Человечеству мала одна планета.
                </div>
                <div class="alert alert-success" role="alert">
                  Мы сделаем обитаемыми безжизненные пока планеты.
                </div>
                <div class="alert alert-danger" role="alert">
                  И начнем с Марса!
                </div>
                <div class="alert alert-warning" role="alert">
                  Присоединяйся!
                </div>
                </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def show_form():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Форма</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">На участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Послевузовское</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof1" id="инженер-исследователь" value="инженер-исследователь">
                                          <label class="form-check-label" for="male">инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof2" id="пилот" value="пилот">
                                          <label class="form-check-label" for="male">пилот</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof3" id="строитель" value="строитель">
                                          <label class="form-check-label" for="male">строитель</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof4" id="экзобиолог" value="экзобиолог">
                                          <label class="form-check-label" for="male">экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof5" id="врач" value="врач">
                                          <label class="form-check-label" for="male">врач</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof6" id="инженер по терраформированию" value="инженер по терраформированию">
                                          <label class="form-check-label" for="male">инженер по терраформированию</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof7" id="климатолог" value="климатолог">
                                          <label class="form-check-label" for="male">климатолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof8" id="специалист по радиационной защите" value="специалист по радиационной защите">
                                          <label class="form-check-label" for="male">специалист по радиационной защите</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof9" id="астрогеолог" value="астрогеолог">
                                          <label class="form-check-label" for="male">астрогеолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof10" id="гляциолог" value="гляциолог">
                                          <label class="form-check-label" for="male">гляциолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof11" id="инженер жизнеобеспечения" value="инженер жизнеобеспечения">
                                          <label class="form-check-label" for="male">инженер жизнеобеспечения</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof12" id="оператор марсохода" value="оператор марсохода">
                                          <label class="form-check-label" for="male">оператор марсохода</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof13" id="киберинженер" value="киберинженер">
                                          <label class="form-check-label" for="male">киберинженер</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof14" id=штурман" value="штурман">
                                          <label class="form-check-label" for="male">штурман</label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="prof15" id="пилот дронов" value="пилот дронов">
                                          <label class="form-check-label" for="male">пилот дронов</label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                     
                                     
                                     
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="5" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        profs = []
        for i in range(1, 16):
            try:
                a = request.form[f'prof{i}']
                profs.append(a)
            except Exception:
                pass
        print(profs)
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
