# Cat bot generator
![Nyan Cat](https://gist.githubusercontent.com/brudnak/aba00c9a1c92d226f68e8ad8ba1e0a40/raw/e1e4a92f6072d15014f19aa8903d24a1ac0c41a4/nyan-cat.gif)
Follow me at [**@GiveCatImages**](https://twitter.com/GiveCatImages) on Twitter!

This project is a simple bot that will automatically post random cat images on your Twitter account at a scheduled time. The images are chosen from a local database, so that no repeated image is posted.

## Prerequisites
- Python 3
- Tweepy ```pip install tweepy```
- Schedule ```pip install schedule```
- Sqlite3 ```pip install sqlite3```
- Configparser ```pip install configparser```
- A Twitter developer account (with API credenitals) with a bot account created

## How to use
1. Clone or download this repository.
2. Create a new file called `config.ini` in the root directory of the project.
3. Add your Twitter API credentials in the `config.ini` file in the following format: <br>
```
[twitter]
API_key = YOUR_API_KEY
API_secret = YOUR_API_SECRET
access_token = YOUR_ACCESS_TOKEN
access_token_secret = YOUR_ACCESS_TOKEN_SECRET
```
4. Use the database you find most convenient, the code is structured in such a way as to use the public database "https://www.kaggle.com/datasets/crawford/cat-dataset" (through a folder in the same repository with the name "cats" and 6 subfolders)
5. Run the script `create_db.py` to create the database with the images path.
6. Run the script `cat_bot_generator.py`
- The bot will tweet a random image at the set time (default is 3 PM)

## Code explanation
The script "create_db.py" creates a SQLite database called "cat_images.db" and a table called "cat_images". This table contains the following columns:
- id: primary key
- path: path of the image
- name: name of the image
- posted: 0 if the image wasn't posted yet, 1 otherwise.

It also insert the images from the "cats" folder to the table.

The script "cat_bot_generator.py" uses the Tweepy library to interact with the Twitter API. It uses the "schedule" library to schedule the posts. It also connects to the "cat_images.db" database to get a random cat image and marks it as posted after it's posted on Twitter.

##Configuration options
- You can change the time the script tweets by editing the best_time variable in cat_bot_generator.py
- You can set the script to tweet at a different interval by editing the schedule.every().day.at(best_time) in cat_bot_generator.py

## Additional information
- If you want to post the images at a specific interval you can use the library `schedule` or `apscheduler` to schedule 
the script to run at specific intervals.
- If you want to customize the message that gets posted along with the image, you can edit the `status` parameter.
- The script will create a database called `cat_images.db` in the root directory of the project.
Cat Bot Generator
- Make sure you have the necessary permissions to tweet images on the account you're using.
- The script will tweet a new image every time it runs, so it's recommended to set it to run once a day.
- The script will only tweet images that haven't been tweeted before. Once all images have been tweeted, it will stop tweeting.

Have fun tweeting cat images! 🐈



