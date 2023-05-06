

import random
import requests
from flask import Flask, render_template

app = Flask(__name__)

PEXELS_API_KEY = 'PASTE_YOUR_PEXEL_API_KEY'
PEXELS_API_URL = 'https://api.pexels.com/v1/search'


@app.route('/')
def index():
    images = get_random_images()
    return render_template('index.html', images=images)

def get_random_images():
    search_terms = ['nature', 'city', 'animals', 'people', 'technology', 'abstract']
    search_term = random.choice(search_terms)
    params = {
        'query': search_term,
        'per_page': 30,
    }
    headers = {
        'Authorization': PEXELS_API_KEY
    }
    response = requests.get(PEXELS_API_URL, params=params, headers=headers)
    data = response.json()
    return data['photos']

if __name__ == '__main__':
    app.run(debug=True)
