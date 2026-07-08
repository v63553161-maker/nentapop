from flask import Flask, render_template_string

app = Flask(__name__)

# Шаблон для первой (главной) страницы
HTML_PAGE_1 = """
<!DOCTYPE html>
<html>
<head>
    <title>Мой первый сайт</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f0f2f5; }
        .container { background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        h1 { color: #333; }
        p { color: #666; font-size: 18px; }
        .btn { display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 15px; }
        .btn:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Привет!</h1>
        <p>Это моя первая работа</p>
        <a href="/next" class="btn">Далее</a>
    </div>
</body>
</html>
"""

# Шаблон для второй страницы, куда ведет кнопка "Далее"
HTML_PAGE_2 = """
<!DOCTYPE html>
<html>
<head>
    <title>Вторая страница</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #e9f5ff; }
        .container { background: white; padding: 30px; display: inline-block; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        h1 { color: #0056b3; }
        .btn-back { display: inline-block; padding: 10px 20px; background-color: #6c757d; color: white; text-decoration: none; border-radius: 5px; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Ура, ты нажал "Далее"!</h1>
        <p>Тут мог бы быть твой следующий крутой контент.</p>
        <a href="/" class="btn-back">Назад на главную</a>
    </div>
</body>
</html>
"""

# Главная страница (когда просто заходишь на сайт)
@app.route('/')
def home():
    return render_template_string(HTML_PAGE_1)

# Вторая страница (куда перекидывает по кнопке)
@app.route('/next')
def next_page():
    return render_template_string(HTML_PAGE_2)

if __name__ == '__main__':
    # Запуск локального сервера
   if __name__ == '__main__':
    
	app.run(host='0.0.0.0', port=10000)