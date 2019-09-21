# code to count number of times each single zip code is in list
# needs to return a table. Left column is zip code. Right column is going to be count of incidents

import csv
import numpy as np
from collections import Counter

zip_list = []

with open('C:/Users/origa/Documents/socialgood/MLDataAustinTX2015/Crime_Reports_2018.csv') as csv_file:
    reader  = csv.reader(csv_file, delimiter=',')
    for row in reader:
        zip_list.append(row[5])

zip_list = zip_list[1:]

for num in range(len(zip_list)):
    if (zip_list[num] == ''):
  #      print("zip code value not found for this report")
        zip_list[num] = 0
    else:
        zip_list[num] = (int(zip_list[num]))
 #   print(num)

#print(zip_list)

zip_and_counts = []
only_zips = []

for num in range(0, len(zip_list)):

    # print(zip_list.count(78730))
    # zip_list[num] = actual address value. Adding to only zips list
    only_zips.append(zip_list[num])


    # if zip that it's checking is not on list already, then add.
    #print("zips and count")
    if (only_zips.count(zip_list[num]) == 1) and zip_list[num] != 0:
        zip_and_counts.append([zip_list[num], zip_list.count(zip_list[num])])
    else:
        # otherwise, it's on zip list and count already
        continue

#print(zip_and_counts)
#print(len(zip_and_counts))

with open('zips_and_counts.csv', mode='w', newline='') as employee_file:
    writer = csv.writer(employee_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    for num in range(0, len(zip_and_counts)):
        #print(zip_and_counts[num][0])
        writer.writerow([zip_and_counts[num][0], zip_and_counts[num][1], (int(zip_and_counts[num][1] / 1000))+1])
        #print(zip_and_counts[num][1])

