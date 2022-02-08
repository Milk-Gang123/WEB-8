from flask import Flask, url_for

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


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
