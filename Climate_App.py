
# coding: utf-8

# In[ ]:


import numpy as np
import datetime as dt


# In[ ]:


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# In[ ]:


engine = create_engine("sqlite:///../Resources/hawaii.sqlite")


# In[ ]:


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# In[ ]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[ ]:


# Create our session (link) from Python to the DB
session = Session(engine)


# In[ ]:


# Using Flask to create routes
app = Flask(__name__)


# In[ ]:


# Creating flask routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/(start date)<br/>"
        f"/api/v1.0/(start date)/(end date)<br/>"
    )


# In[ ]:


@app.route("/api/v1.0/precipitation")
def prcp():
    """Return all dates and precipitation observations from the last 1 year, 
    convert the query results to a dictionary using date as the key and prcp as the value, 
    and return the JSON representation of this dictionary."""
    year_delta = dt.date.today() - dt.timedelta(days=730)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_delta).all()
    prcp_dict = {}
    prcp_num = 0
    current_date = ""
    for measurement in results:
        prcp_num += 1
        prcp_dict[measurement[0]+f" (measurement {prcp_num})"] = measurement[1]
    return jsonify(prcp_dict)


# In[ ]:


@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    results = session.query(Station.station).all()
    station_list = []
    for station in results:
        station_list.append(station[0])
    return jsonify(station_list)


# In[ ]:


app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the last 2 years."""
    year_delta = dt.date.today() - dt.timedelta(days=730)
    results = session.query(Measurement.tobs).filter(Measurement.date >= year_delta).all()
    tobs_list = []
    for tobs in results:
        tobs_list.append(tobs[0])
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def calc_temps(start=None, end="2018-10-07"):
   

    """TMIN, TAVG, and TMAX for a list of dates.

Args:
        start (string): A date string in the format %Y-%m-%d
        end (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Create a dictionary from the row data and append to a list of all temperatures
    temps_list = []
    for temp in results:
        temps_dict = {}
        temps_dict["minimum"] = results[0][0]
        temps_dict["average"] = results[0][1]
        temps_dict["maximum"] = results[0][2]
        temps_list.append(temps_dict)
    return jsonify(temps_dict)


if __name__ == '__main__':
    app.run(debug=False)

