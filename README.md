# YouTube Video Summarizer (Gemini Pro) : GeminiYT-Scribe

## Acknowledgement
I would like to extend my sincere thanks to  [Krish Naik](https://github.com/krishnaik06)  for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>

## About the Project
This project is a YouTube video summarizer built with Streamlit that uses Google Gemini Pro (via the Generative AI API) to generate concise summaries from video transcripts. When a user inputs a YouTube URL, the app extracts the video ID, fetches the transcript using the `youtube_transcript_api`, and passes it to Gemini with a predefined summarization prompt. The resulting summary and key takeaways are displayed in a clean UI along with the video thumbnail. This tool simplifies consuming long-form video content by offering quick, AI-generated insights.

<br>

## How to Run the Project ?
### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
 git clone https://github.com/SoubhikSinha/GeminiYT-Scribe.git
```

<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create --prefix ./venv python=3.10 -y
```

<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```

<br>  

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```

<br>

### **5. Set Up Google API Key**
Create and paste your Google API key inside  `.env`  file (if not created, create one). Get your API key from  [Google AI Studio](https://aistudio.google.com/app/apikey).

Example  `.env`  file content :
```bash
GOOGLE_API_KEY="your_api_key_here"
```


<br>

### **6. Run the Application**
Start the Streamlit application by running :
```bash
streamlit run app.py
```

<br>

### **7. Play Around !**
Explore the capabilities of the **YouTube Summarizer with Gemini Pro** and experience the power of Large Language Models in action. Just paste any YouTube video link, and let the app fetch the transcript, generate a concise summary, and present key takeaways—automatically. All of this happens in real time through an intuitive Streamlit interface, combining transcript parsing and Google Gemini’s advanced summarization in one seamless flow.
