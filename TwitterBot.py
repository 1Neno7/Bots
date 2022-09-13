from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import snscrape.modules.twitter as sntwitter
from numpy import random
from time import sleep


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/i/flow/login')
        sleep(5)

        # Find username
        email = ''
        while not email:
            try:
                email = bot.find_element(by=By.XPATH, value='//input')
            except Exception as ex:
                sleep(2)
        email.click()
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        sleep(2)

        # Find password
        password = ''
        while not password:
            try:
                password = bot.find_element(
                    by=By.XPATH, value='//input[@type="password"]')
            except Exception as ex:
                sleep(2)
        password.click()
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        sleep(5)

    def like_tweets(self, hashtag):
        bot = self.bot
        latest = hashtag+' -filter:replies'
        while True:
            tweets = []
            limit = 240
            for t in sntwitter.TwitterSearchScraper(latest).get_items():
                if len(tweets) == limit:
                    break
                else:
                    tweets.append(t.url)

            for w in tweets:
                bot.get(w)
                sleeptime1 = random.uniform(5, 11)
                sleeptime2 = random.uniform(10, 16)
                sleep(sleeptime1)
                try:
                    heart = bot.find_element(
                        by=By.XPATH, value='//div[@aria-label="Like"]')
                    heart.click()
                    sleep(sleeptime2)
                except Exception as ex:
                    sleep(sleeptime2)

            sleeptime3 = random.uniform(30, 60)
            sleep(60*sleeptime3)


neno = TwitterBot('your username', 'your password')
neno.login()
neno.like_tweets('your hashtage or topic')
