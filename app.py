from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv

import ai
import grab
import twitter
import persist

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    data = persist.load_data()
    return render_template('index.html', data=data)


@app.route('/completion', methods=['POST'])
def completion():
    url = request.form['url']
    url_text = grab.get_url_text(url)
    pre_prompt = """The following is the text from the HTML of an internet 
    article, can you please write a funny tweet it in the style of Kara 
    Swisher about it? Don't reference yourself."""
    prompt = pre_prompt + url_text
    completion = ai.create_completion(prompt)
    completion_text = completion['choices'][0]['text']
    tweet_text = completion_text + "\n" + url
    repsonse = twitter.create_tweet(tweet_text)
    tweet_id = repsonse.data['id']
    persist.save_data(tweet_id, url, prompt, completion_text)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
