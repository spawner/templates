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
    # add your secret token here
    token = ''
    url = "https://spawnerapi.com/answer/" + token
    data = {'text': question}
    headers = {'Content-type': 'application/json'}
    x = requests.post(url, data=json.dumps(data), headers=headers)
    #print(x.text)
    file='static/response.txt' 
    with open(file, 'w') as filetowrite:
        filetowrite.write(x.text)
    return 'finished dumping'

if __name__ == '__main__':
    app.run(debug=True)
