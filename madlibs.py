from random import choice
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():

    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    answer = request.args.get("answer")
    if answer == "yes":
        print answer
        return render_template("game.html", answer=answer)
    if answer == "no":
        return render_template("goodbye.html", answer=answer)

@app.route('/madlib')
def show_madlib():
    gameperson = request.args.get("gameperson")
    gamenoun = request.args.get("gamenoun")
    gameadj = request.args.get("gameadj")
    gamecolor = request.args.get("gamecolor")
    print "This is the answer:", request.args
    return render_template("madlib.html", 
        gameperson=gameperson, 
        gameadj=gameadj, 
        gamenoun=gamenoun, 
        gamecolor=gamecolor)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
