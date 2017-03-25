from flask import Flask, render_template
from recipes import load_recipes
import random

app = Flask(__name__)

@app.route("/")
def home():
    # first get random ingredients
    items = list(load_recipes.load())
    chosen = []
    num_choose = random.randint(5, 10)
    
    # why not
    if(random.randint(0,10) == 1):
        num_choose = 1

    for i in range(0,num_choose):
        # determine unit 
        el = random.choice(items)
        unit = random.choice(['g', 'kg', 'unit', 'teaspoons'])
        amount = random.randint(1, 20)
        if (el.endswith(('ose','ium'))):
            unit = 'moles'

        chosen.append((el, amount,unit))
    
    # generate steps
    steps = []
    for item in chosen:
        action = random.choice(['Burn', 'Bake', 'Deep-fry', 'Fry', 'Stir-fry', 'Steam', 'Cut', 'Dice', 'Mix'])
        time = 0
        if (action in ['Bake', 'Steam']):
            time = random.randint(5, 10)

        steps.append((action, item[0], item[1], item[2], time))

    return render_template('ingredient.html', items = chosen, steps = steps)

if __name__ == "__main__":
    app.run(debug=True)