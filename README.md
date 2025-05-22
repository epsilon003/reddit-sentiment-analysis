# 📊 Reddit Sentiment Analysis: AI in Education

This project collects Reddit posts related to **"AI in Education"** using the PRAW API and prepares them for sentiment and time series analysis. It supports multiple subreddits and stores structured data in CSV format.

---

## 🧾 Project Structure

```
reddit-sentiment-ai-education/
│
├── data/
│   ├── raw/
│   └── cleaned/
├── src/
│   ├── collect.py
│   ├── cleaning.py
│   └── sentiment.py
├── visuals/
|   └── visualise.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔐 .env Template

Copy this to a file named `.env` in the root directory and fill in your Reddit app credentials:

```env
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=script by u/your_reddit_username
```

> 👉 Never share your `.env` file or push it to GitHub. It's excluded by `.gitignore`.

---

## ⚙️ Setup Instructions

1. **Clone this repository**:
```bash
git clone https://github.com/your-username/reddit-sentiment-analysis.git
cd reddit-data-analysis
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up your environment**:
- Create a `.env` file using the template above.

---

## 🚀 Run the Script

Run the main script to fetch Reddit posts:

```bash
python collect.py
```

This will:
- Search Reddit for posts matching `"AI in education"`
- Across subreddits: `education`, `artificial`, `technology`
- Save the output to `data/raw/reddit_posts.csv`

---

## 🧪 Output Example

Sample columns in the CSV:
- `title`
- `selftext`
- `created_utc`
- `score`
- `subreddit`
- `url`
- `full_text`

You can now use this data for:
- Sentiment analysis using VADER
- Time series analysis with Matplotlib or Seaborn

---

## 📎 License

MIT License

---

## 🙋‍♂️ Questions or Contributions?

Feel free to open an issue or pull request. Collaboration is welcome!
