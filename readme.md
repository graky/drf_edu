# DJANGO REST FRAMEWORK
Тестовый проект с использованием DRF

Суть проекта: объединение фриланс работников в организации (гильдии) с возможностью совместной работы над заказами

## Разворачиваем проект локально
Проект использует python версии 3.9
 - Создаем виртуальное окружение
   ##### virtualenv --python=python3.9 venv
 - Устанавливаем необходимые для работы проекта библиотеки из файла зависимостей
   ##### pip install -r requirements.txt
 - Установить базу данных postgresql
 - В корне проекта создать файл .env 
 - Файл содержит данные необходимые для подключения к БД, имя БД, имя пользователя, пароль, хост, порт
   
```
DATABASE_NAME= db_name
DATABASE_USER= db_user
DATABASE_PASSWORD= db_password
DATABASE_HOST= localhost
DATABASE_PORT = 5432
```
 - Для создания структур в БД, необходимо запустить миграции с помощью команды
   ##### python manage.py migrate
 - Чтобы создать суперпользователя для использования админ панели выполняем команду:
   ##### python manage.py createsuperuser
 - Чтобы запустить проект не локальном сервере выполняем команду:
   ##### python manage.py runserver

# Разделы проекта
 - пользователи /users
 - гильдии /guilds
 - проекты /projects

## Раздел пользователи

Регистрация пользователя /signup
POST
```
{
    "username": "my_username",
    "first_name": "Аким",
    "last_name": "Гребенкин",
    "email": "akimgrebenkin21@gmail.com",
    "password": "SomePassword1337"
}

```
Юзернейм и почта валидируются на уникальность.


Обновление пользователя: 
update_user/<user.pk>/
PUT
```
{
    "email": "newemail@mail.ru",
    "skills": ["python", "sql", "docker"],
    "sex": "M",
    "date_birthday": 2000.15.10
}
```

Просмотр списка пользователей:
/profiles
GET

Ответ:
```
[
    {
        "url": "http://127.0.0.1:8000/users/update_user/8/",
        "username": "Customer",
        "first_name": "Тест",
        "last_name": "сайта",
        "email": "test@test.ru",
        "skills": [],
        "sex": null,
        "date_birthday": null
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/7/",
        "username": "designer",
        "first_name": "Контакт",
        "last_name": "Перкут",
        "email": "design@mail.ru",
        "skills": [],
        "sex": null,
        "date_birthday": null
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/6/",
        "username": "user",
        "first_name": "Евгений",
        "last_name": "Колядин",
        "email": "ek@mail.ru",
        "skills": [
            "graphic_design",
            "web-design",
            "layout"
        ],
        "sex": "M",
        "date_birthday": "1999-10-15"
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/5/",
        "username": "grakky1511",
        "first_name": "Антон",
        "last_name": "Перкут2",
        "email": "albetro@mail.ru",
        "skills": [
            "ak"
        ],
        "sex": null,
        "date_birthday": null
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/3/",
        "username": "grox",
        "first_name": "A",
        "last_name": "G",
        "email": "newemail@mail.ru",
        "skills": [
            "python",
            "sql",
            "docker"
        ],
        "sex": "M",
        "date_birthday": "2000-10-15"
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/2/",
        "username": "first_username",
        "first_name": "Akim",
        "last_name": "Grebenkin",
        "email": "medvedevstepan2000@gmail.com",
        "skills": [],
        "sex": null,
        "date_birthday": null
    },
    {
        "url": "http://127.0.0.1:8000/users/update_user/1/",
        "username": "Emperor",
        "first_name": "Антон",
        "last_name": "Перкут",
        "email": "",
        "skills": [],
        "sex": null,
        "date_birthday": null
    }
]
```


## Раздел гильдии

Создать гильдию /guild
POST
```
{
    "title": "Some guild",
    "description": "some description"
}

```


Добавить пользователя в гильдию: 
guild_member/
POST
```
{
    "role": "Manager",
    "position": "ADMIN",
    "user": 8,
    "guild": 3
}
```
Нужно быть создателем гильдии, либо обладать в ней правами админа


Создать команду в гильдии:
/guild_team
POST

```
{
    "name": "Design team",
    "description": "We do design",
    "leader": 3,
    "guild": 3
}
```

Просмотр созданных гильдий:
/guild
GET

Ответ:
```
[
    {
        "title": "Design and marketing guild",
        "description": "We do design and marketing",
        "creator": {
            "url": "http://127.0.0.1:8000/users/update_user/6/",
            "username": "user",
            "first_name": "Евгений",
            "last_name": "Колядин",
            "email": "ek@mail.ru",
            "skills": [
                "graphic_design",
                "web-design",
                "layout"
            ],
            "sex": "M",
            "date_birthday": "1999-10-15"
        },
        "guild_members": [
            {
                "role": "Manager",
                "position": "ADMIN",
                "user": {
                    "url": "http://127.0.0.1:8000/users/update_user/1/",
                    "username": "Emperor",
                    "first_name": "Антон",
                    "last_name": "Перкут",
                    "email": "",
                    "skills": [],
                    "sex": null,
                    "date_birthday": null
                }
            },
            {
                "role": "Manager",
                "position": "ADMIN",
                "user": {
                    "url": "http://127.0.0.1:8000/users/update_user/8/",
                    "username": "Customer",
                    "first_name": "Тест",
                    "last_name": "сайта",
                    "email": "test@test.ru",
                    "skills": [],
                    "sex": null,
                    "date_birthday": null
                }
            }
        ],
        "teams": [
            {
                "name": "Marketing",
                "description": "We do marketing",
                "leader": 5,
                "team_members": [
                    {
                        "role": "Marketing master",
                        "position": "",
                        "user": {
                            "url": "http://127.0.0.1:8000/users/update_user/3/",
                            "username": "grox",
                            "first_name": "A",
                            "last_name": "G",
                            "email": "newemail@mail.ru",
                            "skills": [
                                "python",
                                "sql",
                                "docker"
                            ],
                            "sex": "M",
                            "date_birthday": "2000-10-15"
                        }
                    }
                ],
                "guild": 3
            },
            {
                "name": "Design",
                "description": "We do design",
                "leader": 2,
                "team_members": [],
                "guild": 3
            }
        ]
    }
]
```

## Раздел проекты

Создать проект /project
POST
```
{
    "title": "New project",
    "description": "New project description"
}

```

Обновить проект, добавить гильдию исполнителя, изменить рабочий статус проекта.
projects/<project.pk>/

PUT
```
{
    "title": "New project",
    "description": "New project description",
    "status": "STARTED",
    "guild": 3
}
```
Нужно быть создателем проекта

Создать отчет о работе, нужно быть участником гильдии, работающей над проектом:
/stage
POST

```
{
    "content": "Work started",
    "link": "https://github.com/graky/drf_edu",
    "project": 1
}
```

Просмотр списка проектов:
/projects
GET

Ответ:
```
[
    {
        "title": "New project",
        "description": "New project",
        "status": "NOT_TAKEN",
        "creator": {
            "url": "http://127.0.0.1:8000/users/update_user/6/",
            "username": "user",
            "first_name": "Евгений",
            "last_name": "Колядин",
            "email": "ek@mail.ru",
            "skills": [
                "graphic_design",
                "web-design",
                "layout"
            ],
            "sex": "M",
            "date_birthday": "1999-10-15"
        },
        "guild": null,
        "created": "2022-04-17T20:42:46.906404Z",
        "stages": []
    },
    {
        "title": "Проект для дизайна",
        "description": "Проект дизайна",
        "status": "STARTED",
        "creator": {
            "url": "http://127.0.0.1:8000/users/update_user/8/",
            "username": "Customer",
            "first_name": "Тест",
            "last_name": "сайта",
            "email": "test@test.ru",
            "skills": [],
            "sex": null,
            "date_birthday": null
        },
        "guild": 3,
        "created": "2022-04-17T19:59:45.151796Z",
        "stages": [
            {
                "id": 3,
                "author": {
                    "url": "http://127.0.0.1:8000/users/update_user/3/",
                    "username": "grox",
                    "first_name": "A",
                    "last_name": "G",
                    "email": "newemail@mail.ru",
                    "skills": [
                        "python",
                        "sql",
                        "docker"
                    ],
                    "sex": "M",
                    "date_birthday": "2000-10-15"
                },
                "content": "We started work",
                "link": "https://github.com/graky/drf_edu",
                "created": "2022-04-17T20:10:03.682836Z",
                "project": 9
            },
            {
                "id": 2,
                "author": {
                    "url": "http://127.0.0.1:8000/users/update_user/3/",
                    "username": "grox",
                    "first_name": "A",
                    "last_name": "G",
                    "email": "newemail@mail.ru",
                    "skills": [
                        "python",
                        "sql",
                        "docker"
                    ],
                    "sex": "M",
                    "date_birthday": "2000-10-15"
                },
                "content": "We started work",
                "link": "https://github.com/graky/drf_edu",
                "created": "2022-04-17T20:10:01.104139Z",
                "project": 9
            }
        ]
    }
]
```


