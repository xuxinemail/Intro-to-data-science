# comparing the admission rate of males and females
import csv
data = []
male_total = 0
female_total = 0
male_admitted = 0
female_admitted = 0
with open('Berkeley.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter = ',')
    for line in reader:
        data.append(line)
for line in data:
    num = int(line['Freq'])
    if line['Gender'] == 'Male':
        male_total += num
        if line['Admit'] == 'Admitted':
            male_admitted += num
    else:
        female_total += num
        if line['Admit'] == 'Admitted':
            female_admitted += num
print male_admitted/float(male_total)
print female_admitted/float(female_total)
