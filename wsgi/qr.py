from flask import Flask,request,Response
import StringIO
import qrcode

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = request.args.get('data')
    if data:
	try:
	    qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 10,
		border = 4,
	    )

	    qr.add_data(data)
	    qr.make(fit=True)
	    img = qr.make_image()
	    out = StringIO.StringIO()
	    img.save(out, 'PNG')
	    return Response(out.getvalue(), mimetype='image/png')
	except:
	    return "Error happened"
    else:
	return app.send_static_file('qr.html')

if __name__ == '__main__':
    app.run(debug = "True")
