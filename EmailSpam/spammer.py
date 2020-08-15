import getpass
import smtplib
import threading
import time

from datetime import datetime

class emailSpammer():

    def configure_settings(self, my_emails, destination_email):
        print('\n--> [Starting Configuration]')
        self.my_emails = my_emails
        self.to = destination_email
        self.total_sent = 0

        self.password = getpass.getpass('[Email Password *Hidden]:')
        self.message = input('[Message]:')
        self.times = input('[Emails Per Account]:')
        self.delay = input('[Delay Between Emails]:')


    def send_email(self, task_number):
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        username = self.my_emails[task_number]
        mail.ehlo()
        mail.starttls()
        mail.login(username, self.password)
        for i in range (int(self.times)):
            mail.sendmail(username, self.to, self.message)
            self.total_sent += 1
            print('[Sent {0} Emails!]'.format(str(self.total_sent)))
            time.sleep(int(self.delay))
        mail.close()


    def start_sending(self):
        print('-->[Starting Jobs]')
        jobs = []
        for task_number in range(len(self.my_emails)):
            job = threading.Thread(target=self.send_email, args=(task_number,))
            jobs.append(job)
            jobs[task_number].start()

