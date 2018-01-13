## HW 1
## SI 364 W18
## 1000 points
from flask import Flask, request
import json
import requests
import html

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

# For Problem 4, I used the Star Wars API - documentation found at: https://swapi.co/documentation.


## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

# PROBLEM 1
@app.route('/class')
def hello_to_class():
	return "Welcome to SI 364!"

# PROBLEM 2
@app.route("/movie/<moviename>")
def get_movie_data(moviename):
	base_url = "https://itunes.apple.com/search"
	params_dict = {"term":moviename,"entity":"movie"}

	response = requests.get(base_url, params=params_dict)

	return response.text 

# PROBLEM 3
@app.route('/question',methods=["GET","POST"])
def enter_favorite_number():
    form_string = """<!DOCTYPE html>
		<html><body>
		<form action="http://localhost:5000/question" method="POST">
        Enter Your Favorite Number:<br>
        <input type="text" name="number" value=""><br>
        <input type="submit" value="SUBMIT">
        </form></body></html>"""

    if request.method == "POST":
        fav_num = request.form["number"]

        double_fav_num = 2*int(fav_num)
        return_string = "Double your favorite number is {}".format(double_fav_num)
        form_string = return_string + form_string

        return form_string
    else:
        return form_string

# PROBLEM 4
@app.route("/problem4form", methods = ["GET", "POST"])
def get_user_info():
	title_string = """<h2>
				Star Wars Character Quiz
				</h2>
				"""
	form_string = """<!DOCTYPE html>
		<html>
			<body>
				<form action="http://localhost:5000/problem4form" method="POST">
  					Enter a number (1-5):<br><br>
  					<input type="text" name="starnum" value=""><br><br>
  					Choose a gadget: <br><br>
  					<input type="radio" name="gadget" value="Lightsaber"> Lightsaber <br>
  					<input type="radio" name="gadget" value="Blaster"> Blaster <br>
  					<input type="radio" name="gadget" value="Bowcaster"> Bowcaster <br><br>
  					<input type="submit" value="SUBMIT">
				</form>
			</body>
		</html>"""

	if request.method == "POST":
		star_num = request.form["starnum"]
		star_gadget = request.form["gadget"]
		base_url = "https://swapi.co/api/people/" + star_num + "/"
		response = requests.get(base_url)

		star_wars_char_dict = json.loads(response.text)
		star_char = star_wars_char_dict["name"]
		star_color = star_wars_char_dict["eye_color"]
		if star_char == "Leia Organa":
			star_color = "blue" # because sorry no one wants a brown lightsaber

		char_string = "Congratulations! You are " + star_char + " and you save the galaxy with a " + star_color + " " + star_gadget + ".<br><br>"

		return title_string + char_string + "May the Force be with you.<br><br>" + form_string
	else:
		return title_string + form_string

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
