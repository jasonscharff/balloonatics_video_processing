import numpy as np
import cv2
import os
import csv
import uuid

OUTPUT_FILENAME = ''
KEYS = ['timestamp', 'mean']

DIRECTORY = '/users/jasonscharff/Desktop/FinalPhotos/'

def analyze_photos():
    for filename in os.listdir(DIRECTORY):
        if filename.endswith('.jpg'):
            timestamp = float(filename.split('_')[0])
            photo = cv2.imread(DIRECTORY + filename)
            if photo is not None:
                mean = photo.mean()
                addValueToCSV({"timestamp" : timestamp, "mean" : mean})


def addValueToCSV(value):
    global OUTPUT_FILENAME
    with open(OUTPUT_FILENAME, 'a') as file:
        writer = csv.DictWriter(file, KEYS)
        writer.writerow(value)


def createCSV():
    global OUTPUT_FILENAME
    OUTPUT_FILENAME = 'photo_means_' + str(uuid.uuid4()) +'.csv'

    with open(OUTPUT_FILENAME, 'wb') as file:
        dict_writer = csv.DictWriter(file, KEYS)
        dict_writer.writeheader()


if __name__ == "__main__" :
    createCSV()
    analyze_photos()