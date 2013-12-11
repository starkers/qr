from flask import Flask,request
import StringIO
import qrcode

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    data = request.args.get('data')
    if data:
	return data
    else:
	return "Hello from k3rnl"

if __name__ == '__main__':
    app.run()
