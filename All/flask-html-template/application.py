from flask import Flask, render_template, request, send_file
import requests
import json 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/', methods = ['POST'])
def search():
    question = request.form['test']
    api_key = ''
    url = "https://spawnerapi.com/answer/" + question + "/" + api_key
    response = requests.get(url)
    var = json.loads(response.text) 
    file='static/response.txt' 
    with open(file, 'w') as filetowrite:
        for i in var:
            filetowrite.write(" ")
            filetowrite.write(i['text'])
    return 'finished dumping'

if __name__ == '__main__':
    app.run(debug=True)
