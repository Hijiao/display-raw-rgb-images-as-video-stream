# 模拟视频流来展示rgb图片
简单的使用`opencv`获取摄像头RGB图像,然后压缩为PNG/JPEG,前端浏览器通过频繁获取图片,模拟成为视频流.类似于动画片.
这个demo包含 HTTP GET和 SocketIO 两种通信模式.

## 前置条件
* 正常工作的摄像头一枚.
* 可以使用opencv读取摄像头

## 使用
   ```shell
   $ python3 flask_video.py
   ```   
   http://localhost:5000/get_demo  通过http get请求来传输图片  
   http://localhost:5000/socktio_demo 通过socketio来传输图片 *推荐*


#  display raw rgb images as video stream
 this is a samplest demo useing `opencv` to capture image(raw RGB24) from camera,
 and encode it to PNG or JPEG,browser dispaly the images frequently so that it looks like just a video stream.

## preparation

* a worked camera
* ```cv2.VideoCapture(0).read()```  works well


## usage
   ```shell
   $ python3 flask_video.py
   ```   
   http://localhost:5000/get_demo  browser get images by HTTP/GET method  
   http://localhost:5000/socktio_demo browser get images on socketio *prefered*
