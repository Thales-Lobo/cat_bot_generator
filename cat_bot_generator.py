import tweepy
import schedule
import sqlite3
import configparser

# General settings
best_time = "15:00"

# Acess keys
#Keys are place as strings in the file "config.ini"
config = configparser.ConfigParser()
config.read("config.ini")

API_key = config["twitter"]["API_key"]
API_secret = config["twitter"]["API_secret"]

access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

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
    cursor.execute("UPDATE cat_images SET posted = 1 WHERE id = ?", (id))
    conn.commit()

# Upload image on Twitter
cat_counter = 0
def tweet_image():
    global cat_counter
    try:
        image = get_cat_image()
        if image:
            cat_counter +=1
            media_id = api.media_upload(image[1]).media_id_string
            api.update_status(status=f"Cat Number {cat_counter}🐈‍⬛", media_ids=[media_id])
            print("Tweet sent successfully!")
            # Mark the image as posted in the database
            mark_image_as_posted(image[0])
        else:
            print("No more images on Database!")
    except Exception as e:
        print("Error on sending tweet: " + str(e))

# Schedules the posts
schedule.every().day.at(best_time).do(tweet_image)

while True:
    schedule.run_pending()
