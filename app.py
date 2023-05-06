import random
import requests
from flask import Flask, render_template

app = Flask(__name__)

RAPIDAPI_KEY = 'API'
RAPIDAPI_HOST = 'reddit-meme.p.rapidapi.com'

@app.route('/')
def index():
    images = get_random_images()
    return render_template('index.html', images=images)

def get_random_images():
    url = f"https://reddit-meme.p.rapidapi.com/memes/trending"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST,
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    images = []
    for post in data:
        if post['url'].endswith(('.jpg', '.png', '.jpeg', '.gif')):
            images.append({'src': {'medium': post['url']}, 'photographer': post['title']})

    # If there are less than 5 images, add duplicates to make it 5
    while len(images) < 5:
        images += images

    return images




if __name__ == '__main__':
    app.run(debug=True)
