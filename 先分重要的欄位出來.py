import csv
a = []
k = []  
b = []
j = 0
with open('output1.csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        j+=1
        index = row[2]+row[3]+row[4] 
        if not (index in k):
            k.append(index)
            a.append(row[4])
            a.append(row[6])
            a.append(row[49])
            a.append(row[50])
            b.append(a)
            a = []
with open('output7.csv', 'w', newline='', encoding="utf-8") as outfile:
    csv_writer = csv.writer(outfile)
    for row in b:
        csv_writer.writerow(row)
