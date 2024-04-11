# RamblerToTelegramRedirector

Данное приложение присылает уведомления в Telegram о новых письмах в почтовом ящике Rambler

## Зависимости проекта

* <h3>python = "3.12"</h3>
* <h3>requests = "2.31.0"</h3>

## Установка зависимостей

Для установки всех необходимых библиотек используйте pip:

<code>pip install -r requirements.txt</code><br/>

    
## Запуск программы

Для начала работы введите свои значения конфигурации в <code>config.py:</code>

<code>MAIL_SERVER = 'imap.rambler.ru'
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
TELEGRAM_BOT_TOKEN = ''
CHAT_ID = ''
REQUESTS_TIME = 300
</code>

Чтобы начать работу с приложением, запустите файл `app.py`.