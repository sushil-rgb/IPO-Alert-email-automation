from classes import MerolaganiScraper, EmailAutomation
import copy


merolagani = MerolaganiScraper()
latest_ipo_news = merolagani.ipo_news()
old_update = copy.deepcopy(latest_ipo_news)
email_receivers = ["rockin_sushil@hotmail.com", "gunz19able@gmail.com", 'sushil.bhandari002@gmail.com']


ipo_alert_email = EmailAutomation()

EmailAutomation().send_email(latest_ipo_news, email_receivers[0], merolagani.ipo_announce_date())