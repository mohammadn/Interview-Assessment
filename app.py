import requests, json
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    url = "https://api.thecatapi.com/v1/images/search"

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'be56993c-fde7-47d2-b419-be691a8b799b'
    }

    response = requests.get(url, headers=headers).json()[0]
    return render_template('index.html', response=response)


@app.route('/voting', methods=["Post"])
def voting():
    url = "https://api.thecatapi.com/v1/votes"
    value = request.args.get('value')

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'be56993c-fde7-47d2-b419-be691a8b799b'
    }

    payload = {
        "image_id": request.args.get('image_id'),
        "sub_id": "default",
        "value": 1
    }

    if value == '0':
        payload["value"] = 0
    payload_dumped = json.dumps(payload)

    requests.post(url, headers=headers, data=payload_dumped)

    return redirect('/')

if __name__ == '__main__':
    app.run()
