# Modelling OECD data

Design a logical data model,
transfer it to a physical data model,
insert the data and finally get some relevant information from it.

The domain is extracted from OECD data (https://data.oecd.org/) and we'll be
looking at Gross Domestic Product (GDP), education, and life expectancy over time.

1. Entity Relationship Diagram

![link to diagram](https://github.com/UsernameDiana/databases_course/blob/master/Modelling%20OECD%20data/ER.pdf)

2. Physical Data model

```
CREATE TABLE Locations(
id INTEGER PRIMARY KEY,
Countrycode VARCHAR
);

CREATE TABLE Subjects(
id INTEGER PRIMARY KEY,
SubjectType VARCHAR
);

CREATE TABLE Education(
location INTEGER REFERENCES Locations(id),
subject INTEGER REFERENCES Subjects(id),
Time VARCHAR,
Value DOUBLE PRECISION
);

CREATE TABLE Life(
location INTEGER REFERENCES Locations(id),
subject INTEGER REFERENCES Subjects(id),
Time VARCHAR,
Value DOUBLE PRECISION
);

CREATE TABLE GDP(
location INTEGER REFERENCES Locations(id),
subject INTEGER REFERENCES Subjects(id),
Meassure_Type VARCHAR,
Time VARCHAR,
Value DOUBLE PRECISION
);
```

3. Find the country whose GDP has grown the most over time and plot the level
   of education on the x axis and the life expectancy on the y axis.