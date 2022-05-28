import os
import time

# Preparing
os.chdir('for_server')
directory = os.listdir()
for i in directory:
    if i != 'index.html':
        os.system(f'rm {i}')
os.chdir(os.pardir)

# Tracking start
os.system("gnome-terminal --command 'python track.py --yolo_model weights/best_final.pt --source videos/fight_small.mp4'")

# Server start
os.chdir('for_server')
os.system("gnome-terminal --command 'python3 -m http.server 9000'")

# Gstreamer start
while 'you_can_start_stream.txt' not in os.listdir():
    time.sleep(5)
os.system("gst-launch-1.0 ximagesrc use-damage=0 xname='result' ! videoconvert ! clockoverlay ! videoscale method=0 "
          "! video/x-raw,width=1280, height=720 ! x264enc bitrate=2048 ! video/x-h264,profile=\"high\" ! mpegtsmux "
          "! hlssink playlist-root=http://localhost:9000 location=segment_%05d.ts target-duration=5 max-files=5")
