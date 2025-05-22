import praw
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

# --- CONFIGURATION ---
load_dotenv()  # Load from .env

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

SEARCH_QUERY = "AI in education"
SUBREDDITS = "education+artificial+technology"
LIMIT = 100
OUTPUT_DIR = "data/raw"
OUTPUT_FILE = f"{OUTPUT_DIR}/reddit_posts.csv"


def initialize_reddit_client():
    """Initialize and return the Reddit API client."""
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    return reddit


def fetch_reddit_posts(reddit, query, subreddits, limit):
    """Fetch Reddit submissions matching the query from given subreddits."""
    subreddit = reddit.subreddit(subreddits)
    posts = []

    for submission in subreddit.search(query, limit=limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
            "score": submission.score,
            "subreddit": submission.subreddit.display_name,
            "url": submission.url
        })

    return posts


def save_posts_to_csv(posts, output_path):
    """Save list of posts to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.DataFrame(posts)
    df["full_text"] = df["title"] + " " + df["selftext"]
    df.to_csv(output_path, index=False)
    print(f"[INFO] Saved {len(df)} posts to {output_path}")


def main():
    reddit = initialize_reddit_client()
    print("[INFO] Reddit client initialized.")
    
    posts = fetch_reddit_posts(reddit, SEARCH_QUERY, SUBREDDITS, LIMIT)
    print(f"[INFO] Fetched {len(posts)} posts.")

    save_posts_to_csv(posts, OUTPUT_FILE)


if __name__ == "__main__":
    main()
