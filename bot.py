import tweepy
import random
import time
import os
from datetime import datetime

# Load Twitter credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Project tweets
projects = {
    "EigenLayer": [
        "Restaking is the meta. Watch EigenLayer’s TVL like a hawk. 📈",
        "If you’re not reading EigenLayer docs, you’re NGMI. #CryptoAlpha",
        "How EigenLayer’s AVS model changes crypto security forever."
    ],
    "LayerZero": [
        "LayerZero is connecting ecosystems faster than bridges ever could. 🌉",
        "ZRO airdrop hype is over — now we watch the builders.",
        "LayerZero’s omnichain thesis will age like fine wine."
    ]
    # Add more projects and tweets here
}

# Accounts to follow
to_follow = ["@LidoFinance", "@Starknet", "@zksync"]  # Add more as needed

if __name__ == "__main__":
    print("🚀 Crypto Foal Bot started at", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # Tweet once per project
    for project, tweets in projects.items():
        tweet = random.choice(tweets)
        timestamp = datetime.now().strftime('%H:%M:%S')
        full_tweet = f"{project}: {tweet} [{timestamp}]"
        
        print(f"📤 Attempting to tweet for {project}...")
        try:
            api.update_status(full_tweet)
            print(f"✅ Tweeted: {full_tweet}")
            time.sleep(5)
        except Exception as e:
            print(f"❌ Error tweeting for {project}: {e}")

    # Follow relevant accounts
    for user in to_follow:
        print(f"👤 Attempting to follow {user}...")
        try:
            api.create_friendship(screen_name=user)
            print(f"✅ Followed {user}")
        except Exception as e:
            print(f"❌ Error following {user}: {e}")
