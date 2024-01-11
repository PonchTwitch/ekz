from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Получаем значения из полей формы
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        x3 = request.form.get('x3')

        # Проверка на пустые поля и нечисловые значения
        if not x1 or not x1.isdigit() or not x2 or not x2.isdigit() or not x3 or not x3.isdigit():
            return render_template('index.html', error='Все поля должны быть заполнены числами')

        # Выполняем расчет
        result = 2 * int(x1) + int(x2) * int(x3)

        # Отображаем результат
        return render_template('result.html', result=result)

    # Если метод GET, отображаем пустую форму
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    