# https://appdividend.com/2022/03/19/python-cv2-videocapture/

import cv2
import gi
import sys
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject  # noqa:F401,F402

# Initializes Gstreamer, it's variables, paths
Gst.init(sys.argv)

#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=540 ! nvoverlaysink" # ok
#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! nvoverlaysink" #ok
DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=540 ! nvoverlaysink" # ok
#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=520 ! format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink" # nope
#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! nvvidconv ! nvegltransform ! nveglglessink -e" # nope
#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! nvvidconv ! nvegltransform ! nvoverlaysink" # nope
#DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1' ! nvvidconv flip-method=0 ! 'video/x-raw,width=960, height=540' ! nvvidconv ! nvegltransform ! nvoverlaysink" # nope

pipeline = Gst.parse_launch(DEFAULT_PIPELINE)
print(f"parsed pipeline: {DEFAULT_PIPELINE}")
bus = pipeline.get_bus()
pipeline.set_state(Gst.State.PLAYING)
loop = GObject.MainLoop()

def on_message(bus: Gst.Bus, message: Gst.Message, loop: GObject.MainLoop):
    mtype = message.type
    """
        Gstreamer Message Types and how to parse
        https://lazka.github.io/pgi-docs/Gst-1.0/flags.html#Gst.MessageType
    """
    if mtype == Gst.MessageType.EOS:
        print("End of stream")
        loop.quit()

    elif mtype == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print(err, debug)
        loop.quit()

    elif mtype == Gst.MessageType.WARNING:
        err, debug = message.parse_warning()
        print(err, debug)

    return True

bus.connect("message", on_message, loop)

try:
    loop.run()
except Exception:
    traceback.print_exc()
    loop.quit()

# Stop Pipeline
pipeline.set_state(Gst.State.NULL)

"""
#while(True):
#    pass
#cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture()

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""
