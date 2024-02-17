import praw
from os import environ, path
from dotenv import load_dotenv
import prawcore

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

reddit = praw.Reddit(
    user_agent='Python:batch-subscribe-v1:v1',
    client_id=environ.get('CLIENT_ID'),
    client_secret=environ.get('CLIENT_SECRET'),
    username=environ.get('USERNAME'),
    password=environ.get('PASSWORD')
)

with open('list.txt', 'r') as f:
    subreddit_list = f.readlines()
    for subreddit in subreddit_list:
        subreddit = subreddit.strip()  # Remove leading/trailing whitespace
        print('Subscribing to', subreddit)
        try:
            reddit.subreddit(subreddit).subscribe()
            print('Subscribed to', subreddit)
        except prawcore.exceptions.Forbidden as e:
            print(f'Error subscribing to {subreddit}: {e}')
        except Exception as e:
            print(f'An error occurred while subscribing to {subreddit}: {e}')


