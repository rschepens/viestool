# Methodiek om bestanden te importeren

import csv
with open('Importlines.csv', 'r', encoding="ISO-8859-1" ) as f: #delimeter zou er aan toegevoegd kunnen worden
    reader = csv.reader(f)
    for row in reader:
        for item in row:
            print(item)

            #print(row[1])

#/home/ruud/Downloads/SampleCSVFile_2kb
#https://stackoverflow.com/questions/3182183/creating-a-list-of-objects-in-python

