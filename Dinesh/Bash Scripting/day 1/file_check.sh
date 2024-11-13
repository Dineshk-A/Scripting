#!/bin/bash
echo "enter filename"
read filename

if [ -e "$filename" ]; then
    echo "$filename exists"
else
    echo "$filename doesnt exists"
fi