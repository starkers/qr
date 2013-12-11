from flask import Flask
import Image

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
    return "Hello from k3rnl"

if __name__ == '__main__':
    app.run()
