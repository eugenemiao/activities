import os
import csv
#importing csv as a library, python has a module of csv

cereal_csv_path = os.path.join('..', 'Resource', 'cereal.csv')

with open(cereal_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    #csvreader is a built in python function. This completes importing the file

    for row in csv_reader:
        if(float(row[7]) >= 5):
            #float is a decimal, like double
            print(row)


