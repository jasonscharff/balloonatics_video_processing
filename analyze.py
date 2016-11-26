from __future__ import division
import numpy as np
import cv2
import os
import csv
import uuid

DIRECTORY = '/users/jasonscharff/Desktop/LaunchVideos/'

KEYS = ['timestamp', 'mean']
FRAME_OUTPUT_FILENAME = ''
VIDEO_OUTPUT_FILENAME = ''


def main():
    for filename in os.listdir(DIRECTORY):
        if filename.endswith('.mp4'):
            print filename
            means = []
            timestamp = float(filename.split('_')[0])
            moving_timestamp = timestamp
            ret = True
            video = cv2.VideoCapture(DIRECTORY + filename)
            fps = 25
            video_mean = []
            while ret == True:
                ret, frame = video.read()
                if frame is not None:
                    frame_mean = frame.mean()
                    means.append({'mean' : frame_mean, 'timestamp' : moving_timestamp})
                    video_mean.append(frame_mean)
                    moving_timestamp += 1/fps
            video_average = reduce(lambda x, y: x + y, video_mean) / len(video_mean)
            video_dictionary = {'mean' : video_average, 'timestamp' : timestamp}
            addArrayToCSV(means, video_dictionary)



def addArrayToCSV(frame_means, video_mean):
    with open(FRAME_OUTPUT_FILENAME, 'a') as file:
        writer = csv.DictWriter(file, KEYS)
        writer.writerows(frame_means)

    with open(VIDEO_OUTPUT_FILENAME, 'a') as file:
        writer = csv.DictWriter(file, KEYS)
        writer.writerow(video_mean)

def createCSV():
    global FRAME_OUTPUT_FILENAME
    global VIDEO_OUTPUT_FILENAME
    FRAME_OUTPUT_FILENAME = 'frame_means_' + str(uuid.uuid4()) +'.csv'
    VIDEO_OUTPUT_FILENAME = 'video_means_' + str(uuid.uuid4()) + '.csv'

    with open(FRAME_OUTPUT_FILENAME, 'wb') as file:
        dict_writer = csv.DictWriter(file, KEYS)
        dict_writer.writeheader()
    with open(VIDEO_OUTPUT_FILENAME, 'wb') as file:
        dict_writer = csv.DictWriter(file, KEYS)
        dict_writer.writeheader()


if __name__ == "__main__" :
    createCSV()
    main()