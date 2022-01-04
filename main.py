import csv

data = []
with open("dataset_2.csv" , "r") as f:
    r = csv.reader(f)
    for i in r:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for i in planet_data:
    i[2] = i[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])
with open("dataset_2_sorted.csv" , "a+") as f:
    r = csv.writer(f)
    r.writerow(headers)
    r.writerows(planet_data)