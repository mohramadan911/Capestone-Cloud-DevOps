from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html = "<h1 style='text-align: center;'>Welcome to Udacity Cloud DevOps. My name is Mohamed Ramadan Issa</h1>"
    return html.format(format)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
