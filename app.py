from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from ai import create_completion
from grab import get_url_text

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    completion = request.args.get('completion')
    return render_template('index.html', completion=completion)

@app.route('/completion', methods=['POST'])
def completion():
    url = request.form['url']
    url_text = get_url_text(url)
    pre_prompt = """The following is the text from the HTML of an internet 
    article, can you please summarize it in the style of Kara Swisher? """
    prompt = pre_prompt + url_text
    completion = create_completion(prompt)
    completion_text = completion['choices'][0]['text']
    return redirect(url_for('index', completion=completion_text))

if __name__ == '__main__':
    app.run(debug=True)
