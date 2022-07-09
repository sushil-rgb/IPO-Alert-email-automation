import smtplib
from bs4 import BeautifulSoup
import requests
from scraper_functions import get_ua
from urllib.error import URLError
from apscheduler.schedulers.blocking import BlockingScheduler
import os


EMAIL_ADDRESS = os.environ.get("USER_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


class MerolaganiScraper:
    def fetch(self):
        print(f"HTTP GET request to https://merolagani.com/Ipo.aspx?type=upcoming")       
        headers ={'User-Agent': get_ua()}
        try:
            res = requests.get("https://merolagani.com/Ipo.aspx?type=upcoming", headers=headers)            
        except URLError as url_error:
            print("Server Not Found")
        else:
            print(f"Status Code || {res}")
        

    def ipo_announce_date(self):
        headers ={'User-Agent': get_ua()}
        res = requests.get("https://merolagani.com/Ipo.aspx?type=upcoming", headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')

        date = soup.find('small', class_='text-muted').text.strip()
        return date

    
    def ipo_news(self):        
        headers ={'User-Agent': get_ua()}
        res = requests.get("https://merolagani.com/Ipo.aspx?type=upcoming", headers=headers)
        soup = BeautifulSoup(res.content, 'lxml')

        try:
            news = soup.find('div', class_='media-body').text.strip()         
        except AttributeError:
            news = "No latest IPO news available"

        return news


class EmailAutomation:
    def send_email(self, email_content, receiver, date):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "NEW IPO ALERT!"
            body = email_content
            
            msg = f"Subject: {subject}\n\n{body}\n\nFirst posted on {date}"

            smtp.sendmail(EMAIL_ADDRESS, receiver, msg)


class Scheduler:
    sched = BlockingScheduler()
    @sched.schduled_job('cron', day_of_week='mon-sun', hour=20)
    def scheduler_email(self, automation_email):
        automation_email

    sched.start()
