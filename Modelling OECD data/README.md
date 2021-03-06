# Modelling OECD data

The domain is extracted from OECD data (https://data.oecd.org/) and we'll be
looking at Gross Domestic Product (GDP), education, and life expectancy over time.

1. Logical Data Model: Entity Relationship Diagram

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
Time VARCHAR
);

CREATE TABLE Life(
location INTEGER REFERENCES Locations(id),
subject INTEGER REFERENCES Subjects(id),
Time VARCHAR
);

CREATE TABLE GDP(
location INTEGER REFERENCES Locations(id),
subject INTEGER REFERENCES Subjects(id),
Time VARCHAR
);
```

3. Least grown country plot of education and life expectancy: Brazil.

![link to plot](https://github.com/UsernameDiana/databases_course/blob/master/Modelling%20OECD%20data/Least%20grown%20country.png)