import tweepy
from secret import *
import random
import time


def login():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api

def tuitear_repetido_random():
    #tuitea linea al azar del archivo
    file = open("remezcla.txt", "r", encoding='utf-8')
    text = file.readlines()
    file.close()
    while True:
        rand = random.randrange(len(text))
        print("Intentando tuitear {}".format(text[rand]))
        try:
            api.update_status(status=text[rand])
            print("tuiteado {}".format(text[rand]))
        except Exception as e:
            print(e.reason)
        time.sleep(1200)


if __name__ == "__main__":
    api = login()
    tuitear_repetido_random()


