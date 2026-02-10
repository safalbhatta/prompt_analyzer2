Prompt Analyzer

A web-based tool that evaluates AI prompts, scores them, identifies issues, and suggests improvements to help users write better prompts.

⸻

Features
	•	Scores prompts out of 10
	•	Highlights issues in the prompt
	•	Suggests improved versions
	•	Simple web interface with Flask

⸻

Tech Stack
	•	Frontend: HTML, CSS, Jinja2
	•	Backend: Python Flask
	•	LLM: LLaMA 3.3 70B via Groq API
	•	Libraries: requests, python-dotenv, markdown
	•	Deployment: Render (optional)
⸻
Installation
git clone https://github.com/safalbhatta/prompt_analyzer2.git
cd prompt_analyzerr
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
⸻
Set your API key in .env:
GROQ_API_KEY=your_api_key_here
⸻
Run the app:
python app.py
Open: http://127.0.0.1:5000
⸻
Usage
	1.	Enter a prompt in the text box
	2.	Click Analyze
	3.	See score, issues, and improved prompt
⸻
Project Structure
app.py
config.py
utils/analyzer.py
templates/
static/
requirements.txt
start.sh
.venv (ignored)
.env (ignored)
⸻
Notes
	•	call_llm() is the function calling LLaMA 3.3 API
	•	.env should never be pushed to GitHub
	•	Llama 3.3 evaluates prompts intelligently
  Author
⸻
Safal Bhatta – Nepal
GitHub: https://github.com/safalbhatta￼
⸻
Live Demo
Check out the **Prompt Analyzer** live at:  
https://prompt-analyzer20.onrender.com
You can try it online without installing anything!


