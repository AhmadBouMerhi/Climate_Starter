# Climate_Starter
If you decid to treat yourself to a long holiday vacation in Honolulu, Hawaii, This projcet helps to plan well for your trip:)

This project analyze the climate on the area and here are the steps:

# Step 1 - Climate Analysis and Exploration

The project uses Python and SQLAlchemy to do basic climate analysis and data exploration of climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
The project uses SQLAlchemy create_engine to connect to sqlite database.
Use SQLAlchemy automap_base() reflects tables into classes and save a reference to those classes called Station and Measurement.

# Precipitation Analysis

The project designs a query to retrieve the last 12 months of precipitation data.
Then select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.

Use Pandas to print the summary statistics for the precipitation data.



# Station Analysis


The project designs a query to calculate the total number of stations and also design a query to find the most active stations. 
The project also lists the stations and observation counts in descending order.
The project uses functions such as func.min, func.max, func.avg, and func.count in the queries.
it designs a query to retrieve the last 12 months of temperature observation data (tobs).


# Step 2 - Climate App

The project designs a Flask API based on the queries that it have just developed.

The FLASK creates the routes.

Routes: /api/v1.0/precipitation



