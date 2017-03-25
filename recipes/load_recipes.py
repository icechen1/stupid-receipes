import csv

ingr_set = set()

def load():
    '''
    with open('recipes/recipes.csv', 'rt') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for line in lines:
            for ingr in line[1:]:
                ingr_set.add(ingr)

    with open('recipes/ingredients.csv', 'wt') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for ing in ingr_set:
            spamwriter.writerow([str(ing)])
    '''
    with open('recipes/ingredients.csv', 'rt') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for line in lines:
            if len(line) > 0:
                ingr_set.add(line[0])

    return ingr_set

