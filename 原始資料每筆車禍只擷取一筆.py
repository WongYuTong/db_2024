import csv
a = []
k = set()
with open('111年度A1交通事故資料.csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        index = (row[2], row[3], row[4])  
        if index not in k:
            k.add(index)
            a.append(row)          
for i in range(1, 13):
    with open(f'111年度A2交通事故資料_{i}.csv', 'r', newline='', encoding="utf-8") as infile:
        reader = csv.reader(infile)
        for row in reader:
            index = (row[2], row[3], row[4])
            if index not in k:
                k.add(index)
                a.append(row)
with open('output1.csv', 'w', newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(a)
