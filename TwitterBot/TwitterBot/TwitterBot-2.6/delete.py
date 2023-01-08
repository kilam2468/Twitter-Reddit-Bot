import os
import time


def rem():
    APP_FOLDER = '/home/ec2-user/tootbot/media'

    totalFiles = 0
    totalDir = 0

    for base, dirs, files in os.walk(APP_FOLDER):
        print('Searching in : ', base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1

    if totalFiles >= 5:
        for f in os.listdir(APP_FOLDER):
            os.remove(os.path.join(APP_FOLDER, f))
            print("Removed Files")
    else:
        print("Less Than 5")
        time.sleep(600)


while True:
    rem()
