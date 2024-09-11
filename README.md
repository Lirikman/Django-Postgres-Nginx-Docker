My first Django project:
" IT-PROFI SERVICE "

В проекте использованы технологии:
- Docker
- Compose
- Django
- Gunicor
- PostgreSQL
- Nginx

Описание проекта.
Сайт Сервисного центра по ремонту компьютеров.

Проект состоит из папок:
- config: содержит конфигурционный файл nginx.cong;
- it_profi: содержит файлы web-приложения;
- файл docker-compose.yml: необходим для запуска и создания веб приложения, базы данных и прокси.

Запуск приложения
- Склонировать приложение с github;
- Собрать контейнер командой: docker-compose build;
- Запустить контейнер командой: docker-compose up.

Web-приложение будет доступно по адресу: http://127.0.0.1:8000

Панель администрирования доступна по адресу: http://127.0.0.1/admin
Доступ к панели администрирования:
Логин - admin
Пароль - it12345

ОПИСАНИЕ САЙТА

Структура сайта.
Данный сайт состоит из двух приложений Main и Users.
В приложении Main реализован весь основной функционал сайта.
В приложении Users реализована система регистрации и авторизации пользователей на сайте.

Данный сайт состоит из вкладок: Главная страница(index), Страница про нас(about), Страница создания заявки(create), Страница со всеми заявками(orders), Страница со статьями(Articles), Авторизация(login);

"Главная страница" содержит общую информацию об услугах сервиса.

"Страница про нас" содержит рекламную информацию и рекомендации для обращения в сервис.

Страница "Cоздание заявки на ремонт", содержит три поля ФИО клиента, номер телефона, Неполадка с ПК, а также кнопку Добавить заявку, для занесения заявки в базу данных.
После создания заявки автоматически создаётся запись в базе данных о новой заявки, а также запись в таблице Все клиенты - реализовано с помощью встроенных сигналов Django - post_save.
Заявки на сайте появляются только после проверки их администратором и активации через панель Администрирования - реализовано с помощью Менеджера моделей IsActive.

Страница "Все заявки" предоставляет пользователю информацию о всех имеющихся заявках. На данной странице отображается только ФИО клиента, неполадка и дата заявки, а номер телефона скрыт из соображений конфиденциальности.
Номер телефона видит только Администратор для распределения заявок мастерам и связи с клиентами.
Для удобства отображения на данной странице настроен постраничный вывод заявок по 5 записей. 

Страница "Авторизация" содержит форму для входа на сайт и кнопку для регистрации новой учётной записи.

Страница "Полезные статьи" содержит различные статьи и полезную информацию о информационных технологиях и прочую полезную информацию.
Для удобства отображения на данной странице настроен постраничный вывод статей по 3 записи.
На странице Полезные статьи реализован функционал по добавлению новых статей - кнопка Добавить статью, работает только для зарегистрированных пользователей сайта.

На странице добавления статьи реализована форма с помощью класса CreateView, содержащая поля Название статьи, Загрузка изображения, Текст статьи, Автор и Дата публикации, а также кнопка для сохранения статьи в базу данных.
Все изображения при добавлении статей сохраняются на сервере в папке MEDIA. 
При отсутствии изображения в форме добавления статьи, устанавливается стандартное изображение. 
На странице каждой статьи реализован функционал по Изменению статьи (с помощью класса UpdateView) и Удалению статьи (с помощью класса DeleteView), работает только для зарегистрированных пользователей.
Статьи на сайте появляются только после проверки администратором сайта - реализовано с помощью Менеджера моделей IsActive.

Для хранения информации о неполадках, заявках, статьях и клиентах создана база данных на основе библиотеки SQLite, содержащая две зависимые таблицы Неполадки, Заявки, и две независимые таблицы Статьи, и Все клиенты.
В проекте создана и настроена запись Администратора (name: admin, pass: 12345) и пользователя (name: Test, pass: test2024) в панель администрирования.
Созданы и добавлены в панель администрирования модели: Неполадки ПК(Problem), Заявки на ремонт('Order'), Статьи ('Article'), Все клиенты ('Clients').
Все варианты неполадок и проблем с ПК, добавляются на сайт Администратором и активируются при необходимости - реализовано с помощью Менеджера моделей IsActive.

Написаны пользовательские команды(commands):
all - для просмотра всех заявок, без необходимости входа в Панель администрирования;
del '№ заявки' - для быстрого удаления выбранной заявки;
new_problem - для быстрого добавления новой неполадки ПК;
initialize_db - для первичной иницлизации БД неполадками (problems);
Для тестирования сайта:
fake_articles 'количество статей' - для генерации фейковых статей и добавления их в БД;
fake_orders 'количество заявок' - для генерации фейковых заявок и добавления их в БД.

На сайте реализована система регистрации и авторизации пользователей с помощью классов LoginView, CreateView и LogoutView.
Настроена система прав и ограничений для неавторизованных пользователей, с помощью миксина - LoginRequiredMixin, и проверки свойства is_authenticated на сайте.
Только Автор статьи может её редактировать и удалять, реализовано с помощью UserPassesTestMixin. 
На сайте также настроена система сообщении с помощью messages framework, выводящая сообщения об успешной операции.

В приложении main создана папка tests для тестирования приложения, содержащая файлы - test_models, test_views, test_forms.
Файл test_models содержит тесты модели Articles(Статьи) - простейшие и с использованием библиотек Faker и Mixer.
Файл test_views содержит тесты представлений(Views) - тесты на проверку доступности get запросы, для авторизованных и неавторизованных пользователей, а также тест на post запрос.
Файл test_forms содержит тесты для формы ArticleForm - проверка валидности данных при вводе в форму и отправки на сервер для записи в БД. Данные тесты написаны с помощью библиотеки Pytest.

В проекте использовался Django Rest framework для написания API.
API проекта доступен по адресу: localhost/api/v1
При написании API были использованы классы ViewSet.
Написаны сериализаторы для моделей Article(Статьи) и Problem(Неполадки)
Настроена система авторизации для пользователей и назначены права доступа (реализовано с помощью миксина IsAdminUser, и пользовательских классов разрешений):
- /articles может просматривать любой пользователь, в том числе неавторизованный;
- добавлять статью в базу может любой авторизованный пользователь;
- редактировать статьи и удалять может только автор или администратор;
- /problem просматривать, добавлять, удалять и редактировать может только Администратор;

В проект добавлен инструмент для отладки - Django debug toolbar, и произведена оптимизация сайта с помощью метода select_related, благодаря чему сократилось количество запросов в БД и время загрузки страниц. 

На данный момент сайт способен принимать заявки на ремонт, записывать их в базу данных, вести базу данных клиентов, а также отображать и скрывать все заявки, статьи на странице сайта.
Сайт позволяет создавать аккаунт на сайте, и тем самым предоставлять дополнительные возможности - написание статей и полезной информации.
Администратор отслеживает все заявки, статьи и всех пользователей зарегистрированных на сайте, редактирует заявки, и при необходимости удаляет или включает их отображение на сайте.

Планируется наполнить сайт дополнительной информацией - местонахождение, контактная информация, отзывы клиентов.
Возможно будет написан функционал для фильтрации статей по категориям и сортировки, поиска информации.
Настроить работу с почтой через SMTP сервер, для отправки сообщений пользователям, и восстановления пароля или рассылки.
Создать форум для общения клиентов, и помощи в нетрудных вопросах связанных с работой и устранением неполадок ПК.

