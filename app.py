from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def home():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)

@app.route("/story")
def show_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)

#stretch goal: Add a dropdown menu to the home page that allows users to
#select a variety of stories, when user clicks on option, bring them to
#the page of inputs, then to story page to display story