#!/bin/bash
echo "Enter the directory path:"
read dir

if [ -d "$dir" ]; then
    echo "Listing all files in '$dir':"
    for file in "$dir"/*; do
        if [ -f "$file" ]; then
            echo "File: $file"
        fi
    done
else
    echo "Directory '$dir' does not exist."
fi
