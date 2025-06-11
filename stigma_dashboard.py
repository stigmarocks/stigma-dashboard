# Stigma Assistant Automation
# Purpose: Daily monitoring and task automation for Stigma & Rockengine

# --- CHECKLIST OF AUTOMATED TASKS ---
# 1. Check Google Alerts and search engine results for new mentions
# 2. Monitor Amazon and JPC product availability for CDs
# 3. Track daily streaming stats from Spotify, Apple Music, Amazon Music
# 4. Track social media followers (TikTok)
# 5. Check sales performance on Amazon, JPC, and music shops
# 6. Send daily summary/report (via email or dashboard)
# 7. Monitor MusicBrainz approval status for Stigma artist entry
# 8. Monitor indexing status of Wikidata entry Q134722090
# 9. Trigger keyword-based alerts for "Second Chance", "Rockengine"
# 10. Store and update soundalike artist comparisons for promotion

# --- STREAMLIT DASHBOARD WITH REAL SPOTIFY DATA ---
import streamlit as st
import requests
import base64

st.set_page_config(page_title="Stigma Dashboard", layout="wide")
st.title("🎸 Stigma Daily Dashboard")

# Spotify API Credentials
client_id = "1a5185bab8a44de7b736e414b0a9ea58"
client_secret = "981684d047f048fd939a5ba15056d323"

# Get access token
auth_str = f"{client_id}:{client_secret}"
b64_auth = base64.b64encode(auth_str.encode()).decode()
token_url = "https://accounts.spotify.com/api/token"
headers = {"Authorization": f"Basic {b64_auth}"}
data = {"grant_type": "client_credentials"}

res = requests.post(token_url, headers=headers, data=data)
token = res.json().get("access_token")

# Fetch Spotify Artist Info
artist_id = "4ZiCBBwuen2axvx4FGng3y"
artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"
auth_headers = {"Authorization": f"Bearer {token}"}

response = requests.get(artist_url, headers=auth_headers)
if response.status_code == 200:
    data = response.json()
    followers = data.get("followers", {}).get("total", "N/A")
    popularity = data.get("popularity", "N/A")
    st.metric("Spotify Followers", followers)
    st.metric("Popularity Score", popularity)
else:
    st.error("❌ Failed to fetch Spotify artist data")

# --- Real TikTok Follower Integration via Apify ---
st.subheader("📱 TikTok Stats")
apify_url = "https://api.apify.com/v2/key-value-stores/YOUR-STORE-ID/records/LATEST?disableRedirect=true"
try:
    tiktok_data = requests.get(apify_url).json()
    tiktok_followers = tiktok_data.get("followers", "N/A")
except:
    tiktok_followers = "Error fetching"
st.metric("TikTok Followers", tiktok_followers)

# --- Placeholder for Apple Music & Amazon Music Streaming Stats ---
st.subheader("🎧 Apple & Amazon Music")
apple_music_streams = "(pending setup)"
amazon_music_streams = "(pending setup)"
st.metric("Apple Music Streams", apple_music_streams)
st.metric("Amazon Music Streams", amazon_music_streams)

# Static content
st.image("https://stigma.rocks/wp-content/uploads/Stigma-Band-Shots-Mattia-Mariotti-PhotoVideo-1830-2-scaled.jpg", use_column_width=True)

st.subheader("📰 Latest Press Mentions")
st.markdown("- HappyMag – *'Second Chance is a thunderous rock reckoning.'*")
st.markdown("- CMM Radio Promo started – more reports expected")

st.subheader("📦 CD Availability")
st.markdown("[Amazon.de – Check Now](https://www.amazon.de/dp/B0FBQSZZXL)")
st.markdown("[JPC.de – Check Now](https://www.jpc.de/jpcng/poprock/detail/-/art/stigma-second-chance/hnum/12308394)")

st.subheader("🎧 Soundalike Artists")
st.markdown("Our sound has been compared to:")
st.markdown("- Judas Priest – for vocal attitude and classic riffs")
st.markdown("- Alter Bridge – for melodic power and modern rock production")
st.markdown("- Stone Sour – for raw emotion, chorus-driven energy")
st.markdown("- Iron Maiden – for rhythm guitar work and thematic lyrics")
st.markdown("- Metallica – for heavy riffs and message-driven music")

st.subheader("🏆 Awards")
st.markdown("- *Lies of War* – Winner at Red Moon Film Festival, NYC")
st.markdown("- *Lies of War* – Awarded at Multi-Dimension Independent Film Festival, London")
st.markdown("- *Lies of War* – Featured at Festival de Cannes (Best of Independent Cinema)")

st.caption("Built and managed by Stigma Assistant 🔧")
