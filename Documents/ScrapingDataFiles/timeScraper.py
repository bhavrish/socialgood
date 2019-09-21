import csv

with open('Crime_Reports_2018.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	
	with open('new_times.csv', 'w') as writeFile:
	    writer = csv.writer(writeFile,delimiter=',')
	    ctr=0
	    for line in reader:
			currTime=line[1]
			currTimeList = currTime.split()
			newTime = currTimeList[1]
			#if ctr<5:
			#	print(newTime)
			#	ctr+=1
			#else:
			#	break
			writer.writerows([[newTime]])
readFile.close()
writeFile.close()
