# https://appdividend.com/2022/03/19/python-cv2-videocapture/

import cv2
import gi
import sys
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject  # noqa:F401,F402
# Initializes Gstreamer, it's variables, paths
Gst.init(sys.argv)

DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=540 ! nvoverlaysink" # ok
# open pipeline
pipeline = Gst.parse_launch(DEFAULT_PIPELINE)

# start pipeline
pipeline.set_state(Gst.State.PLAYING)

# get video sink
sink = pipeline.get_by_name("nvoverlaysink")

# get an image and store to file ttt.png
while True:
    ret, frame = sink.get_last_buffer()
    if ret:
        cv2.imwrite("ttt.png", frame)
        break
    
#cap = cv2.VideoCapture(DEFAULT_PIPELINE, cv2.CAP_GSTREAMER)
pipeline = Gst.parse_launch(DEFAULT_PIPELINE)
#pipeline.get_by_name("nvarguscamerasrc").set_property("sensor_id", 0)

# get an image from the camera


cap = cv2.VideoCapture()


while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
