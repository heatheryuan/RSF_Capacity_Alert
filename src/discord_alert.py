import config
from discord import Webhook, RequestsWebhookAdapter
from rsf_capacity import getChrome, getCapacity
import time
from datetime import datetime
from pytz import timezone
import pytz
from database import write_data

# DISCORD WEBHOOK SETUP
webhook = Webhook.from_url(config.webhook_url, adapter=RequestsWebhookAdapter())

valid_hours = {0: (7, 22), 1: (7, 22), 2: (7, 22), 3: (7, 22), 4: (7, 22), 5: (8, 18), 6: (8, 22)}

def sendAlert(timeout=60, threshold=70):
    chrome = getChrome()
    last = -5
    while True:
        text = getCapacity(chrome)
        capacity = int(text.split("%")[0])
        date = datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        day = int(date.weekday())
        hour = int(date.hour)
        
        time_range = valid_hours.get(day)
        if (time_range[0] <= hour <= time_range[1]):
            if capacity <= threshold and abs(capacity-last) >= 5:
                webhook.send(text)
                last = capacity
            write_data(capacity, date)
        else:
            last = -5
        time.sleep(timeout)

sendAlert()
