# Random_Coffee_Bot
![screenshot](logo.jpg)

## Описание
Проект Random_Coffee_Bot - это телеграм-бот, который каждую неделю (по понедельникам) предлагает встретиться с одним из людей, зарегистрированных в боте в пределах компании.
Бот делает рассылку с именем и фамилией коллеги, с которым вам нужно организовать встречу. Участники выбираются случайным образом, поэтому вы сможете выпить кофе с теми, с кем еще не пересекались по работе. Подтверждать встречи не нужно, участие по желанию.

В боте Random_Coffee_Bot реализовано:
- Регистрация пользователей (при регистрации происходит проверка уникальности домена почты, т.е. зарегистрироваться могут только сотрудники компании).
- Хранение данных пользователей в БД Postgres. Функции работы с БД реализованы асинхронно для повышения производительности.
- использование библиотеки и сервера Redis для кэширования данных, повышения производительности и отказоустойчивости бота.
- Каждый пользователь может приостановить или возобновить участие в рассылках для встреч.
- Автоматические еженедельные рассылки (по понедельникам).
- Смена людей случайным образом, исключая повторения. Алгоритм подбора партнера по кофе устроен так, чтобы исключить повторения. Повторение партнеров возможно только в том случае, если человек уже со всеми повстречался, и с момента последней встречи прошло более полугода.
- Администрирование выполнено двумя способами:
  1. Админ-панель Django (доступ через web-интерфес по адресу: http:+ ip вашего сервера)
  2. Напрямую из телеграм-бота (позволяет блокировать или разблокировать пользователя по его почте).

## Технолгии
- Python 3.9
- Aiogram 3.4
- Redis 5.0
- Django 4.2
- APScheduler 3.10
- PostgreSQL 13.10
- Requests 2.31

## Запуск проекта
1) Выполнить установку проект Random_Coffee_Bot на ваш сервер.

2) В корневой директории проекта <ваш_сервер>/:~random_coffee_bot_andrey создайте файл с переменными окружения .env.
Для этого введите команду: ``` sudo touch .env```.
Далее откройте .env-файл с помощью команды ```sudo nano .env``` и заполните его данными по следующему образцу:

```
# Переменные для PostgreSQL
POSTGRES_DB=test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Переменные для Django-проекта:
SECRET_KEY='django-insecure-7f8jl#&fox9p+zm7@e2!8q66&+%+ex94vwe4razd8t5x+g5!qk'
DEBUG=False
HOST_IP='ip вашего сервера'

# Переменные для телеграм ботa
BOT_TOKEN=ваш токен для бота
REDIS_HOST=redis
REDIS_PORT=6379
ALLOWED_DOMAIN=@groupeseb
```

3) Запускаем Docker-compose командой `sudo docker-compose up` и проверяем на наличие ошибок;

4) Закрываем подключение, чтобы не останавлиать контенеры и подключаемся снова к серверу;

5) Переходим в директорию с проектом и заходим в запущенный Docker контейнер - `sudo docker-compose exec backend bash`;

6) Внутри контейнера создаем суперпользователя: `python django_app.py createsuperuser` и вносим данные;

7) После того как суперпользователь создан, закрываем соединение с сервером и можем проверять работу бота и админ панели (перейдя по ссылке типа http://ip_вашего_сервера/)


### Обращаем Ваше внимание, что BOT_TOKEN вы должны получить заранее самостоятельно при создании и регистрации бот-чата
### в телеграм сервисе по созданию ботов https://t.me/BotFather

## Использование телеграм-бота:
- Для начала работы перейдите в чат Random_Coffee_Bot, нажмите кнопку "Menu" и затем всплывающую кнопку "/start".
- Если вы еще не зарегистрированы, то бот предложит вам ввести свои имя и фамилию. После ввода имени и фамилии введите свою корпоративную почту. После успешной регистрации бот ответит вам сообщением "Вы зарегистрированы"
- После регистрации вы автоматически становитесь участником в рассылках для встреч.
- Если вы не хотите продолжать участие, нажмите кнопку "Приостановить участие". Если же вы желаете продолжить участие,  нажмите кнопку "Возобновить участие".

## Администрирование в админ-панели Django:
Админ-панель Django доступна по адресу: http:+ ip вашего сервера.
При наличии прав администратора в админ-панели доступны следующие возможности:
- Просмотр и управление пользователями чата. Управление включает в себя блокировку/разблокировку пользователя, назначение прав администратора, активизация/деактивизация пользователя, изменение почты и изменение введенного пользователем имени и фамилии, а также удаление пользователя.
- Просмотр и удаление встреч, назначенных телеграм-ботом.
- Просмотр и управление рассылками. Администратор может создавать, редактировать или удалять рассылки. При создании или редактировании рассылки указывается текст, дата и время рассылки.

## Администрирование из телеграм-бота:
Для администрирования напрямую из телеграм-бота необходимо ввести команду ```/admin```. После этого бот предложит доступ к административным функциям через сайт админ-панели (см. выше) или ввести почту пользователя для его блокировки/разблокировки.
После ввода почты пользователя бот предоставит вам данные пользователя (имя и фамилия, никнейм, полное имя в тг) и вариант заблокировать/разблокировать или отменить ваше действие.

## Авторы проекта:
[Стеблев Константин](https://github.com/KonstantinSKS)\
[Тен Алексей](https://github.com/aten88)\
[Бойко Максим](https://github.com/Boikomp)\
[Хлестов Андрей](https://github.com/AndreyKhlestov)\
[Фабиянский Илья](https://github.com/fabilya)\
