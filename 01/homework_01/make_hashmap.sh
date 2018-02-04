#!/usr/bin/env bash

set () {
  echo "$1,$2" >> animals_db
}

get () {
  grep "^$1," animals_db | sed -e "s/^$1,//" | tail -n 1
}