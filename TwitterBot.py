from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import snscrape.modules.twitter as sntwitter
import time
import sys


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)

        # Find login Button
        login = bot.find_element_by_css_selector(
            'a.css-1dbjc4n:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
        login.click()
        time.sleep(5)

        # Find username
        email = bot.find_element_by_css_selector('.r-30o5oe')
        email.click()
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(2)

        # Find password
        password = bot.find_element_by_css_selector('.r-homxoj')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

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
                time.sleep(5)
                try:
                    heart = bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div/div[3]/div[7]/div/div[3]')
                    heart.click()
                    time.sleep(15)
                except Exception as ex:
                    time.sleep(15)

            time.sleep(60*30)


neno = TwitterBot('your username', 'your password')
neno.login()
neno.like_tweets('your hashtag or nitch')
sys.exit()
