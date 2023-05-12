# Приложение по поиску вакансий на hh.ru и superjob.ru с использованием базы данных SQLite

Данное приложение предназначено для поиска вакансий на двух популярных российских сайтах: hh.ru и superjob.ru, с использованием базы данных SQLite. Приложение позволяет выводить топ вакансий по зарплате и удалять результаты поиска.

## Установка

Для установки приложения необходимо выполнить следующие шаги:

1. Склонировать репозиторий с приложением на свой компьютер
   

2. Установить необходимые зависимости
   

3. Создать файл `.env` в корневой директории приложения и добавить переменную окружения:

   SJ_TOKEN=your_sj_secret_key
   

   Где  'SJ_TOKEN' - это секретный ключ для доступа к API superjob.ru. Получить эти данные можно на сайте api.superjob.ru.

   

## Использование

Для запуска приложения необходимо выполнить команду:


python main.py


После запуска приложение предложит пользователю Выбрать платформу для поиска вакансий. После этого приложение выполнит поиск вакансий в зависимости от выбора платформы на сайтах hh.ru и superjob.ru и сохранит результаты в базу данных SQLite.

Пользователь может выбрать одно из следующих действий:

* ввести ключевые слова для поиска вакансий

* Вывести топ вакансий по зарплате указав количество выводимых на экран вакансий

* Удалить результаты поиска
  

## Авторы

* Рапоткин Роман - gadjka@mail.ru
