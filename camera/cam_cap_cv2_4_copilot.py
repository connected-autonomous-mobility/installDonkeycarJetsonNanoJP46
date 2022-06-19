# import csi-camera  
from distutils.ccompiler import gen_lib_options
import cv2
import numpy as np
import time
import os
import sys
import gi
gi.require_version('Gst', '1.0')
from gi.repository import GLib, Gst, GObject  # noqa:F401,F402

# Initializes Gstreamer, it's variables, paths
Gst.init(sys.argv)

# define camera pipeline
DEFAULT_PIPELINE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw,width=960, height=540 ! nvoverlaysink" # ok

# open pipeline
pipeline = Gst.parse_launch(DEFAULT_PIPELINE)
bus = pipeline.get_bus()
# start pipeline
pipeline.set_state(Gst.State.PLAYING)
# start pipeline
loop = GLib.MainLoop()
# start pipeline
pipeline.set_state(Gst.State.PLAYING)
# get video sink
sink = pipeline.get_by_name("nvoverlaysink")
print(sink)
# get an image and show on screen
try:
    # get image from pipeline using gstsink
    loop.run()
except Exception:
    traceback.print_exc()
    loop.quit()

# Stop Pipeline
pipeline.set_state(Gst.State.NULL)
