# this file is create a random generatiuon of data or no.into a csv file (one can think it of as yt like counts generator)
import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value", "total_1", "total_2"]


with open('live_data.csv', 'w') as csv_file: #make csv file in writer mode
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('live_data.csv', 'a') as csv_file:  #make csv to read mode
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "total_1": total_1,
            "total_2": total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-2, 10) #random is used to get random values in b/w specified values
        total_2 = total_2 + random.randint(-6, 50)

    time.sleep(1) #to suspend current execution