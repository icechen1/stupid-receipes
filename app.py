from flask import Flask, render_template, request, send_from_directory, Markup
from recipes import load_recipes
import random
import glob

app = Flask(__name__)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('images', path)

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
    choices = ['Burn', 'Bake', 'Deep-fry', 'Fry', 'Stir-fry', 'Steam', 'Cut', 'Dice', 'Mix']
    timed_choices = ['Burn', 'Bake', 'Deep-fry', 'Fry', 'Stir-fry', 'Steam']
    for item in chosen:
        action = random.choice(choices)
        time = 0
        if (action in timed_choices):
            time = random.randint(5, 10)

        steps.append((action, item[0], item[1], item[2], time))

    # set image
    image_paths = glob.glob("images/*.jpg")
    image = Markup('<div class="image" style="background-size: cover; background-position: center; background-image: url(' + random.choice(image_paths) + ');"></div>')

    return render_template('index.html', items = chosen, steps = steps, image = image)

if __name__ == "__main__":
    app.run(debug=True)
