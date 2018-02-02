#!/usr/bin/env bash

# setting function for bash
db_set () {
  echo "$1,$2" >> database
  #! echo = built in command that prints the arguments given
  #! "$1,$2" = 2 arguments seperated via comma
  #! >> points and appends to a file 'database'
}
db_get () {
  grep "^$1," database | sed -e "s/^$1,//" | tail -n 1
  #! grep = searches first argument in "" in database
  #! tail = always reads from the end
}

# fast, lightweight, simple
# bad searching, Big O(N) 1:1 relationship, no security now restrictions