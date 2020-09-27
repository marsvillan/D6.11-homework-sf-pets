## Установка и запуск локально (все действия через коммандную строку)
  - скачать проект и перейти в директорию проекта
  ```
$ git clone https://github.com/marsvillan/D6.11-homework-sf-pets
$ cd D6.11-homework-sf-pets
```
  - создать виртуальное окружение
  ```
$ python -m venv env
```
  - применить виртуальное окружение
```
### Если у вас Linux:
$ source env/bin/activate
### Если у вас Windows:
$ env\Scripts\activate.bat
```
 - установить зависимости
  ```
$ pip install -r requirements.txt
```

  - запустить сервер
  ```
$ python manage.py runserver
```

## Использование локально
- открыть страницу http://127.0.0.1:8000/
- админка http://127.0.0.1:8000/admin (username: admin, password: pass)

