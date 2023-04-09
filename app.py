import openai
from flask import Flask, render_template, request

openai.api_key = "your-api-key"

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def generate_image():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = openai.Image.create(
            prompt=prompt,
            n=3,
            size="256x256"
        )
        return render_template('index.html', image_url=response['data'][0]['url'])
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
