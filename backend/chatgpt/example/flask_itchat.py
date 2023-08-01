# from flask import Flask, render_template
import itchat
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     # Generate QR code for WeChat login
#     qr_code_url = get_qr_code_url()
#     return render_template('index.html', qr_code_url=qr_code_url)


def get_qr_code_url():
    # Initialize WeChat web login for QR code
    itchat.auto_login(hotReload=True, enableCmdQR=True)
    print(itchat.get_QRuuid())
    return itchat.get_QRuuid()

if __name__ == '__main__':
    get_qr_code_url()

#
# if __name__ == '__main__':
#     app.run(debug=True)
