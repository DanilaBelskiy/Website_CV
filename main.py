import os
import time
import multiprocessing
import subprocess


def server():
    os.chdir('for_server')
    subprocess.run('python3 -m http.server 9000', shell=True)


def tracking():
    subprocess.run('python track.py --yolo_model weights/best_final.pt --source videos/fight_small.mp4', shell=True)


def g_streamer():
    os.chdir('for_server')

    while 'you_can_start_stream.txt' not in os.listdir():
        time.sleep(5)

    subprocess.run(
        "gst-launch-1.0 ximagesrc use-damage=0 xname='result' ! videoconvert ! clockoverlay ! videoscale method=0 "
        "! video/x-raw,width=1280, height=720 ! x264enc bitrate=2048 ! video/x-h264,profile=\"high\" ! mpegtsmux "
        "! hlssink playlist-root=http://localhost:9000 location=segment_%05d.ts target-duration=5 max-files=5",
        shell=True)


os.chdir('for_server')
directory = os.listdir()
for i in directory:
    if i != 'index.html':
        os.system(f'rm {i}')
os.chdir(os.pardir)

p1 = multiprocessing.Process(target=tracking)
p2 = multiprocessing.Process(target=server)
p3 = multiprocessing.Process(target=g_streamer)

p1.start()
p2.start()
p3.start()
