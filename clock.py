from apscheduler.schedulers.blocking import BlockingScheduler
import os
import subprocess
import psycopg2
import urlparse
from deleteplaylist import deleteall
import logging
logging.basicConfig()
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=18, minute=31)
#@sched.scheduled_job('interval', hours=7 , minutes=52)
def scheduled_job():
	
	deleteall()
    
#scheduled_job()dsd

sched.start()

