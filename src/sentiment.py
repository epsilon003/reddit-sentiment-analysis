import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is available
nltk.download("vader_lexicon")

# === CONFIGURATION ===
INPUT_FILE = "data/cleaned/cleaned_reddit_posts.csv"
OUTPUT_FILE = "data/processed/sentiment_reddit_posts.csv"

# === INITIALIZE ANALYZER ===
analyzer = SentimentIntensityAnalyzer()

# === FUNCTION TO CLASSIFY SENTIMENT ===
def classify_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return {"compound": 0.0, "pos": 0.0, "neu": 1.0, "neg": 0.0, "label": "Neutral"}

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    # Label based on compound score
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    scores["label"] = sentiment
    return scores

# === MAIN SCRIPT ===
def main():
    df = pd.read_csv(INPUT_FILE)
    print(f"[INFO] Loaded {len(df)} cleaned posts.")

    # Apply sentiment analysis
    sentiment_results = df["cleaned"].apply(classify_sentiment)
    sentiment_df = pd.json_normalize(sentiment_results)

    # Merge with original dataframe
    df = pd.concat([df, sentiment_df], axis=1)

    # Save to output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"[INFO] Sentiment scores saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
