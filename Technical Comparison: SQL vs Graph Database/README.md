# Assignment 9: Technical Comparison: SQL vs Graph Database

Set up an SQL database of your choice and a Neo4j database.
Initialize the databases with data of an artificial social network.
That network consists of persons, i.e., users of a platform such as LinkedIn,
and endorsements, i.e., the acknowledgment of another person.

## Task

Execute a small experiment in which you compare runtime of various queries on
the two databases and report the measured results.

1. Setup an SQL and a Neo4j database respectively.

2. Import the data from the social network
   (endorsement graph https://github.com/datsoftlyngby/soft2018spring-databases-teaching-material/raw/master/data/archive_graph.tar.gz)
   into a Neo4j database and into an SQL database respectively.

3. Construct queries in SQL and in Cypher, which finds:
   * all persons that a person endorses, i.e., endorsements of depth one.
   * all persons that are endorsed by endorsed persons of a person, i.e., endorsements of depth two.
   * endorsements of depth three.
   * endorsements of depth four.
   * endorsements of depth five.

## Results

The difference in graph and relational database is that relational databases
work with sets while graph databases work with paths. Therefor Graph based
databases are faster at searching for nested relations, but SQL based databases
will work faster in on straight value searches and less deep layers.
