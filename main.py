import os
from find_last_run import find_last_run



last_run = find_last_run()

os.system(f'cp -f runs/track/weights/{last_run}/fight_small.mp4 static/')

os.system('flask run --port=6060')
