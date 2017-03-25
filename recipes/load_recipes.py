import csv

ingr_set = set()

with open('recipes.csv', 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for line in lines:
        for ingr in line[1:]:
            ingr_set.add(ingr)

print(ingr_set)
