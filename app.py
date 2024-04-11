from imaplib import IMAP4_SSL
import time
from config import MAIL_SERVER, MAIL_USERNAME, MAIL_PASSWORD, REQUESTS_TIME
from emailer import check_emails

# Подключение к почтовому серверу
mail = IMAP4_SSL(MAIL_SERVER)
mail.login(MAIL_USERNAME, MAIL_PASSWORD)
mail.select('INBOX')

while True:
    check_emails(mail)
    time.sleep(REQUESTS_TIME)