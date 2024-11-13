#!/bin/bash
echo "Enter the file or directory to backup:"
read source
echo "Enter the backup destination directory:"
read destination

if [ -e "$source" ]; then
    if [ ! -d "$destination" ]; then
        echo "Creating backup directory '$destination'."
        mkdir -p "$destination"
    fi
    cp -r "$source" "$destination"
    echo "Backup of '$source' completed to '$destination'."
else
    echo "Source '$source' does not exist."
fi
