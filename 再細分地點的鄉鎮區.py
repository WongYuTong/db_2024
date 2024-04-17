import csv
a = []
b = []
j = 0
with open('output7.csv', 'r', newline='', encoding="utf-8") as infile:
    reader = csv.reader(infile)
    for row in reader:
        j+=1
        
        r1 = (row[1])[:3]
        for i in range(3,len(row[1])):
            if (row[1])[i] in ("鄉","鎮","區","市"):
                r2 = (row[1])[3:i+1]
                r3 = (row[1])[i+1:]
                a.append([row[0],r1,r2,r3,row[2],row[3]])
                print(j)
                break
z = 0
with open('output8.csv', 'w', newline='', encoding="utf-8") as outfile:
    csv_writer = csv.writer(outfile)
    for row in a:
        csv_writer.writerow(row)
        z+=1
        print(z)
