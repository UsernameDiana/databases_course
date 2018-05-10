# Modelling OECD data

Design a logical data model,
transfer it to a physical data model,
insert the data and finally get some relevant information from it.

The domain is extracted from OECD data (https://data.oecd.org/) and we'll be
looking at Gross Domestic Product (GDP), education, and life expectancy over time.

1. Draw a logical data model.
2. Transfer that logical data model into a physical data model and create the
   necessary tables in PostgreSQL.
3. Load all the data into your database.
4. Find the country whose GDP has grown the most over time and plot the level
   of education on the x axis and the life expectancy on the y axis.