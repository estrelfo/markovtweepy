import tweepy
from secret import *


def login():
    # Login y retorna objeto api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api


def guardar_tuits(user):
    # Guarda los tuits (no retuits ni menciones ni links)
    archivo = open('timeline_{}.txt'.format(user), 'w', encoding='utf-8')
    for t in api.user_timeline(screen_name=user, count=100, tweet_mode='extended'):
        if (not t.retweeted) and ('@' not in t.full_text) and ('t.co' not in t.full_text):
            print("{} \n".format(t.full_text))
            archivo.write("{} \n".format(t.full_text))

    archivo.close()


if __name__ == "__main__":
    api = login()
    guardar_tuits('sjw___bot')
