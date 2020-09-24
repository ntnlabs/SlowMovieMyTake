#!/usr/bin/python
# -*- coding:utf-8 -*-

# *************************
# ** Before running this **
# ** code ensure you've  **
# ** turned on SPI on    **
# ** your Raspberry Pi   **
# ** & installed the     **
# ** Waveshare library   **
# *************************

import os, time, sys, random, math
import ffmpeg
from PIL import Image

def generate_frame(in_filename, out_filename, time, width, height):
    (
        ffmpeg
        .input(in_filename, ss=time)
        .filter('scale', width, height, force_original_aspect_ratio=1)
        .filter('pad', width, height, -1, -1)
        .output(out_filename, vframes=1)
        .overwrite_output()
        .run(capture_stdout=True, capture_stderr=True)
    )

width = 800
height = 480
inputVid = "/home/ntn/SlowMovie/Videos/test.mp4"

frameCount = int(ffmpeg.probe(inputVid)['streams'][0]['nb_frames'])
print("there are %d frames in this video" %frameCount)

#frame = random.randint(0,frameCount)
for frame in range(1, frameCount):
 #frame = 1
 print frame

 time = str(math.trunc(frame*41.666666))
 time = time.zfill(4)
 final_time = "00:00:0"+time[0:1]+"."+time[1:]

#msTimecode = "%dms"%(frame*41.666666)
#print msTimecode
#print time
#print ">>",final_time

 generate_frame(inputVid, '/home/ntn/SlowMovie/grab.jpg', final_time, width, height)

 img = Image.open('/home/ntn/SlowMovie/grab.jpg')
 img = img.convert(mode='1',dither=Image.FLOYDSTEINBERG)
 img.show()
 raw_input("Press Enter to continue...")
