#!/bin/bash


day=$1
cd "$(dirname "$0")"

input_file="python/input/day$day.txt"
py_file="python/day$day.py"

if [ ! -f $input_file ]; then
  cookie=$(cat cookie)
  curl "https://adventofcode.com/2020/day/$day/input" \
    -H "Cookie: $cookie" > $input_file
fi

cp python/dayn.py $py_file
sed -i "s/dayn/day$day/g" $py_file
