#QUES 15. READS DATA

import csv
with open('try.csv','r') as csvfile :
    csv_reader=csv.reader(csvfile)
    rows=[]
    for row in csv_reader:
        rows.append(row)
    print(rows)
