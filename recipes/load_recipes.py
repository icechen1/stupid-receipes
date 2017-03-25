import csv

ingr_set = set()

def load():
    with open('recipes/recipes.csv', 'rt') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for line in lines:
            for ingr in line[1:]:
                ingr_set.add(ingr)

    return ingr_set

