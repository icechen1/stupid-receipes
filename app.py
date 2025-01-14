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
        unit = random.choice(['g', 'kg', 'units', 'teaspoons'])
        amount = random.randint(1, 20)
        if (el.endswith(('ose','ium'))):
            unit = 'moles'

        chosen.append((el, amount, unit))
    chosen.append(('Sriracha', 1, 'teaspoon'))

    # generate steps
    steps = []
    choices = ['Burn', 'Bake', 'Deep-fry', 'Fry', 'Stir-fry', 'Steam', 'Cut', 'Dice', 'Mix']
    timed_choices = ['Burn', 'Bake', 'Deep-fry', 'Fry', 'Stir-fry', 'Steam', 'Mix']
    for item in chosen:
        action = random.choice(choices)
        time = 0
        if (action in timed_choices):
            time = random.randint(5, 10)

        steps.append((action, item[0], item[1], item[2], time))

    # generate steps text
    steps_text = []
    for i,step in enumerate(steps):
        text = step[0] + " the " + step[1]
        if step[4] > 0:
            text += " for " + str(step[4]) + " minutes"

        text += "."
        steps_text.append((i+1, text))

    steps_text.append((len(steps_text)+1, 'Dump everything in a bowl and serve.'))

    # set image
    image_paths = glob.glob("images/*.jpg")
    # windows fix
    chosen_path = random.choice(image_paths)
    chosen_path = chosen_path.replace('\\', '/')
    image = Markup('<div class="image" style="background-size: cover; background-position: center; background-image: url(' + chosen_path + ');"></div>')

    # title
    main = chosen[0][0]
    style1 = main.title()
    style4 = main.title()
    if len(chosen) > 1:
        side = chosen[1][0]
        style1 = main.title() + " with " + side
        style4 = main.title() + " with " + side + " mix"

    style2 = main.title() + " royale"
    style3 = steps[0][0].title() + "ed " + main.title()

    countries = ["Chinese", "Canadian", "American", "French", "African"]
    country = random.choice(countries)

    style5 = country + " " + main.title()
    style6 = country + " " + main.title() + " Fusion"

    title = random.choice([style1, style2, style3, style4, style5, style6])

    return render_template('index.html', items = chosen, steps_text = steps_text, image = image, title = title)

if __name__ == "__main__":
    app.run(debug=True)
