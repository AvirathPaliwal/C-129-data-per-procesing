import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv" , "r") as f:
    r = csv.reader(f)
    for i in r:
        dataset_1.append(i)

with open("dataset_2_sorted.csv" , "r") as f:
    r = csv.reader(f)
    for i in r:
        dataset_2.append(i)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1+headers_2
planet_data = []

for index,item in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("final.csv" , "a+") as f:
    r = csv.writer(f)
    r.writerow(headers)
    r.writerows(planet_data)
