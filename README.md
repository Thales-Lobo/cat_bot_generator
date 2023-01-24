# Cat Bot Generator

This project allows you to post pictures of cats on your Twitter account automatically. The images are chosen from a 
local database, so that no repeated image is posted.

## Prerequisites
- Python 3.x
- Tweepy library for Python
- SQLite3 library for Python
- A Twitter Developer account and API credentials

## How to use

1. Clone or download this repository.
2. Create a new file called `config.ini` in the root directory of the project.
3. Add your Twitter API credentials in the `config.ini` file in the following format:
[twitter]
API_key = YOUR_API_KEY
API_secret = YOUR_API_SECRET
access_token = YOUR_ACCESS_TOKEN
access_token_secret = YOUR_ACCESS_TOKEN_SECRET

Copy code
4. Run the command `python main.py` to start the script.

**Note**: 
- The script will search for a directory called `cats` in the root directory and will extract all the `.jpg` files from 
the subdirectories of the `cats` folder and adds them to the database.
- The script will then select a random image from the database that hasn't been posted yet and post it on your Twitter 
account.
- The script will then mark the image as posted in the database so that it won't be posted again.

## Additional information
- If you want to post the images at a specific interval you can use the library `schedule` or `apscheduler` to schedule 
the script to run at specific intervals.
- If you want to customize the message that gets posted along with the image, you can edit the `status_message` 
variable in the `main.py` file.
- If you want to change the directory where the script should search for images, you can edit the `image_directory` 
variable in the `main.py` file.
- The script will create a database called `cat_images.db` in the root directory of the project.
Cat Bot Generator
Welcome to the Cat Bot Generator! This project allows you to create a bot that periodically posts images of cats on 
Twitter. The images are taken from a reliable cat image database, and the bot ensures that the same image is not posted 
multiple times.

Getting Started
Prerequisites
Python 3.6 or higher
Tweepy library (can be installed with pip install tweepy)
A reliable cat image database (instructions on how to set this up can be found in the next section)
A Twitter developer account and API keys (instructions on how to obtain them can be found in the next section)
Setting up the cat image database
Create a folder called "cats" in the same directory as the .py file.
Inside the "cats" folder, create 7 folders named "CAT_00", "CAT_01", "CAT_02", "CAT_03", "CAT_04", "CAT_05", and "CAT_06".
Inside each of these folders, place the cat images that you wish to use (only .jpg files will be used).
Run the script "create_cat_db.py" to create the cat image database. The database will be in the format of a SQLite 
database called "cat_images.db" and will have 3 columns: "id", "path", and "name".
Setting up Twitter API keys
Go to the Twitter Developer Portal and sign in with your Twitter account.
Apply for Elevated access via the Developer Portal, You can learn more here: 
https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve
Create a new project and generate the API keys (Consumer Key, Consumer Secret, Access Token, Access Token Secret).
Create a file called "config.ini" in the same directory as the .py file.
Inside the "config.ini" file, add the following lines:
Copy code
[twitter]
API_key = "your consumer key here"
API_secret = "your consumer secret here"
access_token = "your access token here"
access_token_secret = "your access token secret here"
Running the bot
Run the script "cat_bot.py" to start the bot.
The bot will periodically post a random image of a cat from the database on your Twitter account.
Note: The bot will only post images that have not been posted before. Once an image is posted, its "posted" value in the 
database will be set to 1.

Authors
Thales Lobo - Initial work - Thales-Lobo
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
Thanks to the developers of the Tweepy library for making it easy to interact with the Twitter API.
Thanks to the creators of the reliable cat image database for providing the images used in this project.
Note
Make sure to insert your credentials in the config.ini file before runing the script.
