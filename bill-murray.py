from flask import Flask, render_template
import requests

app = Flask(__name__)


# http://api.themoviedb.org/3/person/1532/combined_credits?api_key=29dbe7a4a74a2fdd215eb48f50630c3f&format=json

@app.route('/')
def index():
    data = requests.get("http://api.themoviedb.org/3/person/1532/combined_credits",
                        params=dict(api_key="29dbe7a4a74a2fdd215eb48f50630c3f")).json()
    return render_template('index.html', movies=data['cast'])


if __name__ == '__main__':
    app.run()
