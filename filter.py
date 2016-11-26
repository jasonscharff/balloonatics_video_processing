import csv
import numpy

TAKEOFF_TIME = 1479754087.56587
LAND_TIME = 1479759819.80346

def filterCSVForFlight(filename):
    with open(filename, 'r') as original_file:
        reader = csv.DictReader(original_file)
        with open ('filtered_' + filename, 'w') as new_file:
            writer = csv.DictWriter(new_file, reader.fieldnames)
            writer.writeheader()
            for row in reader:
                timestamp = float(row['timestamp'])
                if timestamp < LAND_TIME and timestamp > TAKEOFF_TIME:
                    writer.writerow(row)

def convergeCSV(filename, elements_per_median):
    with open(filename, 'r') as original_file:
        reader = csv.DictReader(original_file)
        with open ('converged_' + filename, 'w') as new_file:
            writer = csv.DictWriter(new_file, ['timestamp', 'mean'])
            writer.writeheader()
            timestamps = []
            values = []
            i = 0
            for row in reader:
                timestamps.append(float(row['timestamp']))
                values.append(float(row['mean']))
                if i >= elements_per_median:
                    median_timestamp = numpy.median(timestamps)
                    median_value = numpy.median(values)
                    timestamps = []
                    values = []
                    writer.writerow({'timestamp' : median_timestamp, 'mean' : median_value})
                    i = 0
                i += 1


#filterCSVForFlight('video_means.csv')

convergeCSV('frame_means.csv', 3000)