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

## Setup container for neo4j:

```
docker run \
    -d --name neo4j \
    --rm \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --volume=$(pwd)/import:/import \
    --volume=$(pwd)/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/class \
    --env=NEO4J_dbms_security_procedures_unrestricted=apoc.\\\*,algo.\\\* \
    --env=NEO4J_dbms_memory_pagecache_size=6G \
    --env=NEO4J_dbms_memory_heap_max__size=10G \
    neo4j

docker exec neo4j sh -c 'neo4j stop'
docker exec neo4j sh -c 'rm -rf data/databases/graph.db'

docker exec neo4j sh -c 'neo4j-admin import \
    --nodes:Person /import/social_network_nodes.csv \
    --relationships:ENDORSES /import/social_network_edges.csv \
    --ignore-missing-nodes=true \
    --ignore-duplicate-nodes=true \
    --id-type=INTEGER'
```


## Results

The difference in graph and relational database is that relational databases
work with sets while graph databases work with paths. Therefor Graph based
databases are faster at searching for nested relations, but SQL based databases
will work faster in on straight value searches and less deep layers.
