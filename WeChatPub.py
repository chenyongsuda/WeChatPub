from flask import Flask
from flask import request
import hashlib

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/weixin')
def weixin():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')
    token = "chenyongsuda"

    data_list = [token, timestamp, nonce]
    sorted(data_list)
    sha1 = hashlib.sha1()
    map(sha1.update, data_list)
    hashcode = sha1.hexdigest()
    print "handle/GET func: hashcode, signature: ", hashcode, signature
    if hashcode == signature:
        return echostr
    else:
        return ""


if __name__ == '__main__':
    app.run()
