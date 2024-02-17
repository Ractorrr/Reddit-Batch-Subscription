
# Reddit Batch Subscribe

![Reddit Batch Subscribe](https://img.shields.io/badge/License-MIT-green)

Dive into Reddit communities like never before! With this Python script, you can effortlessly subscribe to multiple subreddits in one go using the PRAW (Python Reddit API Wrapper) library. Whether you're exploring niche interests or broadening your horizons, this tool simplifies the process. Handle any bumps along the way gracefully with built-in exception handling. Start discovering your Reddit journey today!

## Prerequisites

- Python 3.x
- PRAW library (`pip install praw`)

## Getting Started

1. **Clone the repository**:

```
git clone https://github.com/your_username/reddit-batch-subscribe.git
cd reddit-batch-subscribe
```

2. **Install dependencies**:

```
pip install -r requirements.txt
```

3. **Obtain Reddit API credentials**:

    - Go to the Reddit website and sign in to your account.
    - Navigate to the [Reddit Apps page](https://www.reddit.com/prefs/apps).
    - Click on the "Create App" or "Create Another App" button.
    - Fill in the details for your application (name, description, etc.).
    - Select "script" as the app type.
    - Enter a redirect URI (e.g., `http://localhost:8080`).
    - Click on "Create app" to generate your client ID and client secret.
    - Note down your client ID and client secret.

4. **Create a `.env` file** in the project directory and add your Reddit API credentials:

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USERNAME=your_reddit_username
PASSWORD=your_reddit_password
```

5. **Prepare a list of subreddits**:

Create a text file (e.g., `list.txt`) with one subreddit name per line.

6. **Run the script**:

```
python batch_subscribe.py
```

The script will read the list of subreddits from the `list.txt` file and attempt to subscribe to each subreddit. Any errors encountered during the process will be displayed in the console.

## License

This project is licensed under the terms of the MIT License. See the [LICENSE](LICENSE) file for details.
