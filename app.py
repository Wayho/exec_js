import os
import json

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for,make_response)
from sign import MusicApi_kuwo_sign
import execjs

app = Flask(__name__)

#apt-get install node-babel7 -y

@app.route('/')
def index():
    print('Request for home page received')
    return make_response("Flask! v1.0.8")

@app.route('/info')
def info():
    ii = execjs.get()
    print(ii)
    return make_response(str(ii))

@app.route('/music/songlist')
def music_songlist():
    server = request.values.get('server', '')
    t_id = request.values.get('id', '')
    reqid = MusicApi_kuwo_sign().get_ReqId
    if server and t_id:
        if server == 'kugou':
            resp = {'msg': 'kugou'}
        elif server == 'wyy':
            resp = {'msg': 'wyy'}
        elif server == 'qqmusic':
            resp = {'msg': 'qq'}
        elif server == 'kuwo':
            resp = {'msg': reqid}
        else:
            resp = {'msg': '暂不支持此平台'}
    else:
        resp = {'msg': '缺少必要参数'}
    response = make_response(json.dumps(resp, ensure_ascii=False, separators=(",", ":")))
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/mp3')
def mp3():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'mp3.mp3', mimetype='audio/mpeg')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
