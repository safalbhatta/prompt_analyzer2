from flask import Flask, render_template, request
import markdown
from utils.analyzer import call_mixtral, extract_score
import config

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    user_prompt = ""
    result = ""
    score = None

    if request.method == "POST":
        user_prompt = request.form.get("user_prompt")

        prompt = f"""
Analyze this prompt:

1. Give SCORE out of 10  
2. Explain issues  
3. Suggest better version  

PROMPT:
{user_prompt}
"""

        try:
            response = call_mixtral(prompt)
            result = markdown.markdown(response)
            score = extract_score(response)

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template(
        "index.html",
        user_prompt=user_prompt,
        result=result,
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)