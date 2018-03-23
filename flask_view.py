
import base64


from flask import Flask
from flask_socketio import SocketIO
import tools
from flask import render_template
import logging
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)

socketio = SocketIO()

socketio.init_app(app)

emit_flag = False


def just_emit():
    print("-------thread start--------")
    global emit_flag
    while True:
        if emit_flag:
            raw_data = tools.shot()

            image_data = "data:image/jpeg;base64,%s" % base64.b64encode(raw_data).decode('ascii')
            logging.debug("emit one image by SocketIO ,image size : %.02f kb" %(len(image_data)/1000))

            socketio.emit('image', {'msg': image_data},
                          namespace='/chat', broadcast=True)
        eventlet.sleep(0.1)


@socketio.on('connect', namespace='/chat')
def connect():
    print("connect")
    global emit_flag
    emit_flag = True


@socketio.on('disconnect', namespace='/chat')
def disconnect():
    print("disconnect")
    global emit_flag
    emit_flag = False


@app.route('/get_demo')
def get_demo():
    return render_template('get_demo.html', name="max")


@app.route('/socketio_demo')
def socketio_demo():
    return render_template('socketio_demo.html')


@app.route('/shot_once')
def shot_once():
    image_data = tools.shot()
    logging.debug("received shot_once request by GET,image size : %.02f kb" %(len(image_data)/1000))
    response = app.make_response(image_data)
    response.headers['Content-Type'] = 'image/JPEG'
    return response


eventlet.spawn(just_emit)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
