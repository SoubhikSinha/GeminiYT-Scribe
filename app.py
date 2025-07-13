import streamlit as st
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

import re

def extract_video_id(youtube_url):
    """
    Extracts the video ID from a standard or shortened YouTube URL.
    """
    # Match full and short YouTube URLs
    match = re.search(r"(?:v=|be/)([a-zA-Z0-9_-]{11})", youtube_url)
    if match:
        return match.group(1)
    else:
        return None

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini system prompt
prompt = """
You are a YouTube video summarization assistant.
Your task is to summarize the content of a YouTube video based on its transcript.
You will be provided with the transcript of the video.
Your response should be a concise summary of the video content and provide key takeaways (points) from the video.
Content limit is 200-250 words. The transcript text will be appended to your prompt.
"""

# Extract transcript from YouTube video URL
def extract_transcript(youtube_url):
    video_id = extract_video_id(youtube_url)
    if not video_id:
        st.error("Invalid YouTube link format.")
        return None
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id) # Fetch transcript data
        transcript = " ".join([segment["text"] for segment in transcript_data]) # Combine segments into a single string
        return transcript
    except Exception as e:
        st.error(f"Transcript Error: {e}") # Handle errors in fetching transcript
        return None

# Generate summary using Gemini
def generate_summary(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt + transcript_text) # Append transcript to the prompt
    return response.text

# Streamlit UI
st.title("🎬 YouTube Video Summarizer (Gemini Pro)")
youtube_url = st.text_input("Enter YouTube Video URL:")

if youtube_url:
    video_id = extract_video_id(youtube_url)
    if video_id:
        st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", caption="Video Thumbnail")
    else:
        st.warning("Invalid YouTube link. Please provide a valid video URL.")

if st.button("Get Summary"):
    with st.spinner("Fetching transcript and summarizing..."):
        transcript = extract_transcript(youtube_url)
        if transcript:
            summary = generate_summary(transcript, prompt)
            st.markdown("## 📝 Video Summary:")
            st.write(summary) 