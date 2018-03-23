import cv2

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s %(message)s'
                    # format='%(asctime)s %(name)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    )
logging.getLogger("socketio").setLevel(logging.WARNING)
logging.getLogger("engineio").setLevel(logging.WARNING)

camera = None


def check_and_open_camera():
    global camera
    if camera is None or not camera.isOpened():
        print("capture0 is None or closed ,try open it ")
        camera = cv2.VideoCapture(0)
    return True


def shot():
    global camera
    if check_and_open_camera():
        ret0, img0 = camera.read()
        # ret, buf = cv2.imencode('.png', img0, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        ret, buf = cv2.imencode('.JPEG', img0, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
        # logging.debug(" shot image  -- > size %.02f kb" %(len(buf)/1000))
        return buf.tostring()
    else:
        logging.error("can not open camera")
        raise Exception("can not open camera")


if __name__ == '__main__':
    print(shot())
