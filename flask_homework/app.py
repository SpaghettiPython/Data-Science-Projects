import pandas as pd
import sqlalchemy
import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from pprint import pprint
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

latest_Date = (session.query(Measurement.date).order_by(Measurement.date.desc())).first()

l_d_s = str(latest_Date[0]).split("-")
l_year = int(l_d_s[0])
l_month = int(l_d_s[1])
l_day =  int(l_d_s[2])

l_y_d_s = dt.date(l_year, l_month, l_day) - dt.timedelta(days=365)

@app.route("/")
def home():
    return (f"Welcome to the Surfs Up! API<br/>"
            f"Available routes:<br/>"
            f"/api/v1.0/precipitaton<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/temperature<br/>"
            f"/api/v1.0/start/2016-07-16<br/>"
            f"/api/v1.0/start_end/2016-07-16/2016-07-21<br/>")

@app.route("/api/v1.0/precipitaton")
def precipiation():

    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > l_y_d_s).order_by(Measurement.date).all()
    precipitation_list = []

    for rslt in results:
        precipitation_dictionary = {rslt.date: rslt.prcp, "Station": rslt.station}
        precipitation_list.append(precipitation_dictionary)
    return jsonify(precipitation_list)

@app.route("/api/v1.0/stations")
def station_list():
    station_list = session.query(Station.station).all()
    all_stations = list(np.ravel(station_list))
    return jsonify(all_stations)

@app.route("/api/v1.0/temperature")
def temperature():
    results = (session.query(Measurement.date, Measurement.tobs, Measurement.station).filter(Measurement.date > l_y_d_s).order_by(Measurement.date).all())
    temperature_list = []
    for rslt in results:
        temperature_dict = {rslt.date: rslt.tobs, "Station": rslt.station}
        temperature_list.append(temperature_dict)
    return jsonify(temperature_list)

@app.route('/api/v1.0/start/<start_Date>')
def start(start_Date):
    results =  (session.query(*[Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]).filter(func.strftime("%Y-%m-%d", Measurement.date) >= start_Date).group_by(Measurement.date).all())
    dates_list = []                       
    for rslt in results:
        date_dict = {}
        date_dict["Date"] = rslt[0]
        date_dict["Minimum_Temperature"] = rslt[1]
        date_dict["Average_Temperature"] = rslt[2]
        date_dict["High_Temperature"] = rslt[3]
        dates_list.append(date_dict)
    return jsonify(dates_list)

@app.route('/api/v1.0/start_end/<start_Date>/<end_Date>')
def startEnd(start_Date, end_Date):
    results =  (session.query(*[Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]).filter(func.strftime("%Y-%m-%d", Measurement.date) >= start_Date).filter(func.strftime("%Y-%m-%d", Measurement.date) <= end_Date).group_by(Measurement.date).all())
    dates_list = []                       
    for rslt in results:
        date_dict = {}
        date_dict["Date"] = rslt[0]
        date_dict["Minimum_Temperature"] = rslt[1]
        date_dict["Average_Temperature"] = rslt[2]
        date_dict["High_Temperature"] = rslt[3]
        dates_list.append(date_dict)
    return jsonify(dates_list)

if __name__ == "__main__":
    app.run(debug=True)