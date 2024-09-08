#!/bin/bash

# Name of the ZIP file
ZIP_FILE="thesis_results.zip"

# List of paths
PATHS=(
    "returned_prompts/"
    "results/"
    "benchmarks/evalplus/results/"
    "benchmarks/codefuse-evaluation/codefuseEval/result/"
    "benchmarks/PurpleLlama/CybersecurityBenchmarks/results/"
)

# Function to move files into a ZIP archive
compress() {
    echo "Moving files to $ZIP_FILE..."

    # Move the directories into the ZIP file
    zip -rm $ZIP_FILE "${PATHS[@]}"
    
    # Check if the operation was successful
    if [ $? -eq 0 ]; then
        echo "Files moved and compressed into: $ZIP_FILE"
    else
        echo "Error while moving and compressing files!"
        exit 1
    fi
}

# Function to decompress and restore the files to their original directories
decompress() {
    echo "Restoring files from $ZIP_FILE..."

    # Check if the ZIP file exists
    if [ ! -f $ZIP_FILE ]; then
        echo "ZIP file $ZIP_FILE not found!"
        exit 1
    fi

    # Extract the ZIP file
    unzip -o $ZIP_FILE
    
    # Check if the operation was successful
    if [ $? -eq 0 ]; then
        echo "Files restored successfully!"
    else
        echo "Error while restoring files!"
        exit 1
    fi
}

# Check the arguments passed to the script
case "$1" in
    compress)
        compress
        ;;
    decompress)
        decompress
        ;;
    *)
        echo "Usage: $0 {compress|decompress}"
        exit 1
        ;;
esac
