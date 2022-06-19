
# https://eva-support.adlinktech.com/docs/get-stream-data-from-pipeline-1


# git clone https://github.com/IST-EVA-Support/EVA-Sample.git
# cd EVA-Sample

def establish_thread_pipeline():
    print('Start establish pipeline in thread.')
    # GStreamer init and declare the pipeline
    Gst.init(sys.argv)
    pipeline = Gst.Pipeline().new("example-pipeline")

    # Start to declare the elements
    ## element: appsrc
    src = Gst.ElementFactory.make("appsrc", "src")
    caps = Gst.caps_from_string("video/x-raw,format=BGR,width=640,height=480,framerate=30/1")
    src.set_property('caps', caps)
    src.set_property('blocksize', 640*480*3)
    src.connect('need-data', need_data)
    src.connect('enough-data', enough_data)
    ## element: clockoverlay
    clockoverlay = Gst.ElementFactory.make("clockoverlay", "clockoverlay")
    ## element: videoconvert
    videoconvert = Gst.ElementFactory.make("videoconvert", "videoconvert")
    ## element: appsink
    sink = Gst.ElementFactory.make("appsink", "sink")
    sink.set_property('emit-signals', True)
    sink.connect('new-sample', new_sample, None)
    ### elements
    pipeline_elements = [src, clockoverlay, videoconvert, sink]

    establish_pipeline(pipeline, pipeline_elements)

    bus = pipeline.get_bus()

    # allow bus to emit messages to main thread
    bus.add_signal_watch()

    # Start pipeline
    pipeline.set_state(Gst.State.PLAYING)

    loop = GLib.MainLoop()

    bus.connect("message", on_message, loop)

    try:
        print("Start to run the pipeline in thread.\n")
        loop.run()
    except Exception:
        traceback.print_exc()
        loop.quit()

    # Stop Pipeline
    pipeline.set_state(Gst.State.NULL)
    del pipeline
    print('pipeline stopped.\n')

caps = Gst.caps_from_string("video/x-raw,format=BGR,width=640,height=480,framerate=30/1")
src.set_property('caps', caps)
src.set_property('blocksize', 640*480*3)
src.connect('need-data', need_data)
src.connect('enough-data', enough_data)
# ... code omitted
sink.set_property('emit-signals', True)
sink.connect('new-sample', new_sample, None)
