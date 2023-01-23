import tweepy
import schedule
import time
import random
import sqlite3
import configparser

best_time = "00:30"
time_zone = "Brazil"

# Acess keys
config = configparser.ConfigParser()
config.read('config.ini')

API_key = config['twitter']['API_key']
API_secret = config['twitter']['API_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentication
auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Database connection
conn = sqlite3.connect("cat_images.db")
cursor = conn.cursor()

# Gets new cat image
def get_cat_image():
    cursor.execute("SELECT * FROM cat_images WHERE posted = 0 ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

# Marks the image as already chosen
def mark_image_as_posted(id):
    cursor.execute("UPDATE cat_images SET posted = 1 WHERE id = ?", (id,))
    conn.commit()

# Upload image on Twitter
def tweet_image():
    try:
        image = get_cat_image()
        if image:
            # Faz o upload da imagem no Twitter
            api.update_with_media(image[1])
            print("Tweet enviado com sucesso!")
            # Marca a imagem como postada no banco de dados
            mark_image_as_posted(image[0])
        else:
            print("Não há mais imagens para postar.")
    except Exception as e:
        print("Erro ao enviar tweet: " + str(e))

# Schedules the postsca
schedule.every().day.at(best_time).do(tweet_image)

while True:
    schedule.run_pending()
