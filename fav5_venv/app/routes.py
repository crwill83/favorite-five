from app import app
from flask import render_template
from config import Config

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/first_five')
def firstFive():
    foods = ['Pizza','Ice Cream','Burgers','Pastries','BBQ']
    return render_template('first_five.html', my_foods=foods)



@app.route('/second_five')
def secondFive():
    movies = ['The Princess Bride','The Sandlot','The Matrix','The Dark Knight','Princess Mononoke']
    return render_template('second_five.html', my_movies=movies)



@app.route('/third_five')
def thirdFive():
    places = ['Montana De Oro','Bishop/s Peak','Mount Whitney','Monterey Bay Aquarium','Sulphur Creek Ranch']
    return render_template('third_five.html', my_places=places)



@app.route('/fourth_five')
def fourthFive():
    kids = ['Emma','Jared','Laura','Tessa','Sarah']
    return render_template('fourth_five.html', my_kids=kids)



@app.route('/fifth_five')
def fifthFive():
    games = ['7 Days to Die','Atlas','Conan Exiles','Minecraft: Modded','Payday 2']
    return render_template('fifth_five.html', my_games=games)




