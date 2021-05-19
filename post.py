import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login, password, subject, recipients, header):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.header = header
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"

    def send_message(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)  # identify ourselves to smtp gmail client
        ms.ehlo()  # secure our email with tls encryption
        ms.starttls()  # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, msg['To'], msg.as_string())

        ms.quit()
        return

    def receive(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP, 993)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', self.header, criterion)

        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


itm = Email('something@gmail.com', 'something', 'Subject', ['something@mail.ru'], None)

if __name__ == '__main__':
    itm.send_message('Hello')
    print(itm.receive())
