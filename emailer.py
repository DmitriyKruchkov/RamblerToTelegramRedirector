from base64 import b64decode
from email.header import decode_header
from requests import get
import email
from config import TELEGRAM_BOT_TOKEN, CHAT_ID


# Функция для отправки уведомления в Telegram
def send_telegram_message(message):
    get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}")


# Функция для проверки новых писем и отправки уведомления
def check_emails(mail_server):
    result, data = mail_server.search(None, 'UNSEEN')
    if data[0]:
        for num in data[0].split():
            result, data = mail_server.fetch(num, '(RFC822)')
            email_message = email.message_from_bytes(data[0][1])
            sender = decode_header(email_message['From'])[0][0].decode()
            if email_message['Subject']:
                subject = decode_header(email_message['Subject'])[0][0].decode()
            else:
                subject = "No Title"
            text = ""
            for part in email_message.walk():
                if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                    text = b64decode(part.get_payload()).decode()
            message = f'New email from: {sender}\nSubject: {subject}\nText: {text}'
            send_telegram_message(message)
