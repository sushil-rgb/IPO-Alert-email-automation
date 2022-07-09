from apscheduler.schedulers.blocking import BlockingScheduler
from classes import MerolaganiScraper, EmailAutomation
import copy


ipo_alert_email = EmailAutomation()
merolagani = MerolaganiScraper()
posted_date = merolagani.ipo_announce_date()
latest_ipo_news = merolagani.ipo_news()
old_update = copy.deepcopy(latest_ipo_news)
email_receivers = ["rockin_sushil@hotmail.com", "gunz19able@gmail.com", 'sushil.bhandari002@gmail.com']
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=22.2)
def scheduled_job():
    ipo_alert_email.send_email(latest_ipo_news, email_receivers[0], posted_date)


sched.start()

