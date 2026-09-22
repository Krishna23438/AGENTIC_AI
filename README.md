# 🎥 AI YouTube Video Analyzer

An **Agentic AI-powered YouTube Video Analyzer** built with **Streamlit, Agno, Groq, and YouTubeTools**.

The application allows users to provide a YouTube video URL and automatically generate an AI-powered analysis containing video insights, summaries, key points, timestamps, and structured information.

## 🚀 Live Demo

🔗 **Streamlit App:**
`YOUR_STREAMLIT_APP_URL`

> Replace `YOUR_STREAMLIT_APP_URL` with your actual Streamlit deployment URL after deployment.

---

## ✨ Features

* 🎥 Analyze YouTube videos using an AI agent
* 🤖 Agentic AI powered by **Agno**
* ⚡ Fast AI inference using **Groq**
* 📺 YouTube video analysis using **YouTubeTools**
* 📝 Generate structured video reports
* ⏱️ Identify important timestamps and sections
* 💡 Extract key learning points and insights
* 📄 Download the generated analysis as a PDF
* 🔗 Open the analyzed video directly on YouTube
* 🕘 Keep a history of recently analyzed videos
* 🎨 Modern dark-themed Streamlit interface
* 📱 Responsive Streamlit UI

---

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Application development         |
| Streamlit     | Web application UI              |
| Agno          | AI agent framework              |
| Groq          | LLM inference                   |
| YouTubeTools  | YouTube video analysis          |
| ReportLab     | PDF report generation           |
| python-dotenv | Environment variable management |

---

## 🏗️ Project Structure

```text
AGENTIC_AI/
│
├── ui.py
├── youtube_analyzer.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> ⚠️ Do not upload `.env` to GitHub. Add it to `.gitignore`.

---

## 🔄 How It Works

```text
                 YouTube URL
                      │
                      ▼
              Streamlit Interface
                      │
                      ▼
                Agno AI Agent
                      │
              ┌───────┴────────┐
              ▼                ▼
        Groq LLM          YouTubeTools
              │                │
              └───────┬────────┘
                      ▼
                Video Analysis
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Summary     Key Points   Timestamps
                      │
                      ▼
                 PDF Report
```

---

## 📋 Requirements

Python **3.10+** is recommended.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

The application requires a **Groq API key**.

### Local Development

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/Krishna23438/AGENTIC_AI.git
```

Move into the project directory:

```bash
cd AGENTIC_AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run ui.py
```

The application will open in your browser.

---

## ☁️ Deploy on Streamlit Community Cloud

This project can be deployed directly from GitHub using **Streamlit Community Cloud**.

### 1. Push the project to GitHub

Make sure the repository contains:

```text
ui.py
youtube_analyzer.py
requirements.txt
README.md
.gitignore
```

### 2. Open Streamlit Community Cloud

Go to:

https://share.streamlit.io/

Sign in with your GitHub account.

### 3. Create the application

Select:

```text
Repository: Krishna23438/AGENTIC_AI
Branch: main
Main file path: ui.py
```

Streamlit Community Cloud lets you select the repository, branch, and entrypoint file during deployment.

### 4. Add your secret

Open **Advanced settings → Secrets** and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Do not put your API key directly into the GitHub repository. Streamlit provides a Secrets interface for deployment configuration.

### 5. Deploy

Click **Deploy**.

After deployment, Streamlit provides a `streamlit.app` URL that you can add to the **Live Demo** section above.

---

## 📦 Dependencies

The project uses:

```text
streamlit
reportlab
python-dotenv
agno
groq
youtube-transcript-api
```

These dependencies should be listed in `requirements.txt` so Streamlit Community Cloud can install them when creating the deployment environment.

---

## 🔐 Security

Never commit API keys or other secrets to GitHub.

Make sure `.gitignore` contains:

```text
.env
venv/
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

For Streamlit deployment, use Streamlit's Secrets configuration instead of committing credentials to the repository.

---

## 📸 Application Workflow

1. Paste a YouTube video URL.
2. Click **Analyze**.
3. The AI agent processes the video.
4. Review the generated report.
5. View key information and timestamps.
6. Download the analysis as a PDF.

---

## 🎯 Use Cases

This project can be useful for:

* 📚 Students analyzing educational videos
* 👨‍💻 Developers analyzing technical tutorials
* 🎓 Researchers extracting information from lectures
* 📖 Learners creating study notes
* 🎥 Content analysis
* ⚡ Quickly understanding long YouTube videos

---

## 🔮 Future Improvements

Potential future enhancements include:

* 🌍 Multi-language video analysis
* 🎙️ Voice-based interaction
* 🧠 More detailed semantic video understanding
* 📊 Visual analytics and charts
* 📚 Automatic study-note generation
* ❓ AI-generated questions and answers
* 📝 Automatic quiz generation
* 🔍 Improved timestamp detection
* 💬 Interactive chat with the analyzed video
* 📑 More advanced PDF report formatting

---

## 👨‍💻 Author

**Krishna Gupta**

GitHub:
https://github.com/Krishna23438

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

````

### One change after deployment

Once Streamlit gives you your actual URL, replace:

```text
YOUR_STREAMLIT_APP_URL
````

with something like:

```text
https://your-app-name.streamlit.app
```

You can also add a Streamlit badge to the README. Streamlit officially supports adding a badge that links directly to your deployed application.

For your repository, I'd put the **Live Demo + badge near the top**, because someone viewing your GitHub project can immediately open and test your AI application.
