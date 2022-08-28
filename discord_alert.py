from discord import Webhook, RequestsWebhookAdapter
import config
import rsf_capacity
import time

# DISCORD WEBHOOK SETUP

# set up webhook using the url in config.py (not given in repo - private data)
webhook = Webhook.from_url(config.webhook_url, adapter=RequestsWebhookAdapter())
# send test message to url

# writes data, infinite loop
# planning to daemonize this code to run forever on an EC2 instance or something
# would also like to not have to host it in some random df

# todo: make the bot send alerts to separate roles using discord webhook
# different roles for different threshold/timeout values
# currently only one setting
# better messages

# another idea: use regression or smth to predict rsf crowd for the next 15/30min

# todo: time check, don't send alerts when the RSF isn't open


def sendAlert(timeout=15, threshold=50):
    chrome = rsf_capacity.getChrome()
    while True:
        text = rsf_capacity.getCapacity(chrome)
        webhook.send(text)
        time.sleep(timeout)

sendAlert()