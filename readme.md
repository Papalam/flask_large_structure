Для разработки
==============

1. Расcкоментировать строки в docker-compose.yml отвечающие за порты у сервиса db
2. Поменять в файле web/flask/config.py секцию MYSQL_DATABASE_HOST = 'db', вместо db указать IP локального компьютера

### Как запускать flask для отладки ###
В терминале выполняем команды:

    cd web/flask/
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run