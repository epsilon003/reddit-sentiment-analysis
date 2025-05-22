import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === CONFIGURATION ===
INPUT_FILE = "data/processed/sentiment_reddit_posts.csv"
PLOT_DIR = "outputs/"
os.makedirs(PLOT_DIR, exist_ok=True)

# === LOAD DATA ===
df = pd.read_csv(INPUT_FILE, parse_dates=["created_utc"])
print(f"[INFO] Loaded {len(df)} posts for visualization.")

# === PREPROCESS ===
# Round timestamps to day
df["date"] = df["created_utc"].dt.date

# Group by date
grouped = df.groupby("date").agg(
    avg_compound=("compound", "mean"),
    pos_count=("label", lambda x: (x == "Positive").sum()),
    neg_count=("label", lambda x: (x == "Negative").sum()),
    neu_count=("label", lambda x: (x == "Neutral").sum()),
    total_posts=("label", "count")
).reset_index()

# === PLOT 1: AVERAGE COMPOUND OVER TIME ===
plt.figure(figsize=(12, 6))
sns.lineplot(data=grouped, x="date", y="avg_compound", marker="o")
plt.axhline(0, color="gray", linestyle="--", linewidth=1)
plt.title("Average Compound Sentiment Over Time")
plt.ylabel("Avg Compound Sentiment Score")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/avg_sentiment_over_time.png")
print("[INFO] Saved avg_sentiment_over_time.png")

# === PLOT 2: STACKED SENTIMENT COUNTS ===
plt.figure(figsize=(12, 6))
plt.stackplot(
    grouped["date"],
    grouped["pos_count"],
    grouped["neu_count"],
    grouped["neg_count"],
    labels=["Positive", "Neutral", "Negative"],
    colors=["#4caf50", "#9e9e9e", "#f44336"],
    alpha=0.8
)
plt.title("Sentiment Distribution Over Time")
plt.ylabel("Number of Posts")
plt.xlabel("Date")
plt.legend(loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{PLOT_DIR}/sentiment_distribution_over_time.png")
print("[INFO] Saved sentiment_distribution_over_time.png")
