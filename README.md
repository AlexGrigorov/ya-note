Для загрузки заготовленных новостей после применения миграций выполните команду:
```bash
python manage.py loaddata news.json
```
py -3.12 -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db.json

python manage.py runserver

Тесты в Django запускаются командой 
python manage.py test (-v 1...3)

# Запустить все тесты проекта.
python manage.py test 

# Запустить только тесты в приложении news.
python manage.py test news

# Запустить только тесты из файла test_trial.py в приложении news.
python manage.py test news.tests.test_trial

# Запустить только тесты из класса Test
# в файле test_trial.py приложения news.  
python manage.py test news.tests.test_trial.Test

# Запустить только тест test_example_fails
# из класса YetAnotherTest в файле test_trial.py приложения news.
python manage.py test news.tests.test_trial.YetAnotherTest.test_example_fails 

# Развернутый отчет о результатах теста:
python manage.py test -v 1(2 или 3)
python manage.py test -v 3
