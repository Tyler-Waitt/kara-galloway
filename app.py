from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from ai import create_completion

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    completion = request.args.get('completion')
    return render_template('index.html', completion=completion)

@app.route('/completion', methods=['POST'])
def completion():
    prompt = request.form['prompt']
    completion = create_completion(prompt)
    print(completion)
    completion_text = completion['choices'][0]['text']
    return redirect(url_for('index', completion=completion_text))

if __name__ == '__main__':
    app.run(debug=True)
