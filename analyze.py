import numpy as np
import cv2
import os
import csv
import uuid

DIRECTORY = '/users/jasonscharff/Desktop/LaunchVideos/'

KEYS = ['timestamp', 'mean']
OUTPUT_FILE_NAME = ''


def main():
    for filename in os.listdir(DIRECTORY):
        means = []
        timestamp = float(filename.split('_')[0])
        ret = True
        video = cv2.VideoCapture(DIRECTORY + filename)
        fps = 30
        count = 0
        while ret == True:
            ret, frame = video.read()
            if frame is not None:
                means.append({'mean' : frame.mean(), 'timestamp' : timestamp})
                timestamp += 1/fps
        addArrayToCSV(means)



def addArrayToCSV(means):
    with open(OUTPUT_FILE_NAME, 'a') as file:
        writer = csv.DictWriter(file, KEYS)
        writer.writerows(means)

def createCSV():
    global OUTPUT_FILE_NAME
    OUTPUT_FILE_NAME = 'means_' + str(uuid.uuid4()) +'.csv'
    with open(OUTPUT_FILE_NAME, 'wb') as file:
        dict_writer = csv.DictWriter(file, KEYS)
        dict_writer.writeheader()


if __name__ == "__main__" :
    createCSV()
    main()