import csv
import pandas as pd

d1 = [] 
d2 = [] 
with open("bright_stars.csv",'r',encoding='utf8') as f: 
    csv_reader = csv.reader(f) 
    for i in csv_reader: 
        d1.append(i)

with open("unit_convert_stars.csv",'r',encoding='utf8') as f: 
    csv_reader = csv.reader(f) 
    for i in csv_reader: 
        d2.append(i)

h1 = d1[0]
h2 = d2[0]
h3 = h1 + h2
p1 = d1[1:]
p2 = d2[1:]
p = []

for i in p1: 
    p.append(i)

for i in p2: 
    p.append(i)

with open("total_stars.csv",'w',encoding='utf8') as f:
    a = csv.writer(f)
    a.writerow(h3)
    a.writerows(p)

