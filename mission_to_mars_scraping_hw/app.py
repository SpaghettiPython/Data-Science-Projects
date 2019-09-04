from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def home():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict=mars_dict)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape():

    # Run scrapped functions
    mars_dict = mongo.db.mars_dict
    mars_data = mission_to_mars.nasa_text()
    mars_data = mission_to_mars.mars_images()
    mars_data = mission_to_mars.mars_weather()
    mars_data = mission_to_mars.mars_facts()
    mars_data = mission_to_mars.mars_hemispheres()
    mars_dict.update({}, mars_data, upsert=True)

    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
