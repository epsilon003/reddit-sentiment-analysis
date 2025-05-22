import pandas as pd
import re
import os
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# === CONFIGURATION ===
INPUT_FILE = "data/raw/reddit_posts.csv"
OUTPUT_FILE = "data/cleaned/cleaned_reddit_posts.csv"


# === TEXT CLEANING FUNCTION ===
def clean_text(text):
    if not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove mentions, hashtags, digits, and non-letter characters
    text = re.sub(r"@\w+|#\w+|\d+|[^a-zA-Z\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords
    words = [word for word in text.split() if word not in stop_words]

    return " ".join(words)


# === MAIN CLEANING SCRIPT ===
def main():
    # Load raw Reddit data
    df = pd.read_csv(INPUT_FILE)
    print(f"[INFO] Loaded {len(df)} rows from {INPUT_FILE}")

    # Apply cleaning function to 'full_text'
    df["cleaned"] = df["full_text"].apply(clean_text)

    # Optionally filter out short cleaned posts (< 5 words)
    df = df[df["cleaned"].str.split().str.len() >= 5]

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Save cleaned data
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"[INFO] Saved cleaned data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
