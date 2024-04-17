import csv
a = []
with open('1050429_行政區經緯度(toPost).csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        a.append(row)
        
b = [] 
with open('output7.csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        b.append(row[1])
d = []
for i in range(len(a)):
    c = 0
    for j in range(len(b)):
        if ((a[i])[0]) in b[j]:
            d.append(j)
            c+=1
    a[i].append(c)
    for x in range(len(d)-1,0,-1):
        b.pop(d[x])
    d = []
    print(a[i])
z = 0
with open('鄉鎮區發生車禍筆數.csv', 'w', newline='', encoding="utf-8") as outfile:
    csv_writer = csv.writer(outfile)
    for row in a:
        csv_writer.writerow(row)
        z+=1
        print(z)
