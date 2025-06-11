import streamlit as st
import requests

st.set_page_config(page_title="Stigma Dashboard", layout="wide")
st.title("🎸 Stigma Daily Dashboard")

# Spotify Token (replace with your real token)
token = "YOUR_SPOTIFY_BEARER_TOKEN"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://api.spotify.com/v1/artists/4ZiCBBwuen2axvx4FGng3y", headers=headers)

if response.status_code == 200:
    data = response.json()
    followers = data.get("followers", {}).get("total", "N/A")
    popularity = data.get("popularity", "N/A")
    st.metric("Spotify Followers", followers)
    st.metric("Popularity Score", popularity)
else:
    st.error("Failed to fetch Spotify data – check token")

st.image("https://stigma.rocks/wp-content/uploads/Stigma-Band-Shots-Mattia-Mariotti-PhotoVideo-1830-2-scaled.jpg", use_column_width=True)

st.subheader("📰 Latest Press Mentions")
st.markdown("- HappyMag – *'Second Chance is a thunderous rock reckoning.'*")
st.markdown("- More via Google Alerts coming soon")

st.subheader("📦 CD Availability")
st.markdown("[Amazon.de – Check Now](https://www.amazon.de/dp/B0FBQSZZXL)")
st.markdown("[JPC.de – Check Now](https://www.jpc.de/jpcng/poprock/detail/-/art/stigma-second-chance/hnum/12308394)")

st.caption("Built by Rockengine for Stigma | Managed by Stigma Assistant 🔧")
