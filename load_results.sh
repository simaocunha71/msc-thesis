#!/bin/bash

# Name of the ZIP file
ZIP_FILE="mbpp_results.zip"

# Default list of paths
DEFAULT_PATHS=(
    "returned_prompts/"
    "results/"
    "benchmarks/evalplus/results/"
    "benchmarks/codefuse-evaluation/codefuseEval/result/"
    "benchmarks/PurpleLlama/CybersecurityBenchmarks/results/"
)

# Function to search for 'mbpp' subdirectories
find_mbpp_paths() {
    MBPP_PATHS=()
    
    # Find all 'mbpp' directories inside 'returned_prompts'
    for dir in $(find returned_prompts -type d -name "mbpp"); do
        MBPP_PATHS+=("$dir")
    done
    
    # Add additional fixed paths if necessary
    MBPP_PATHS+=("results/mbpp" "benchmarks/evalplus/results/")
}

# Function to search for 'humaneval_x' subdirectories
find_humaneval_x_paths() {
    HUMANEVAL_X_PATHS=()
    
    # Find all 'humaneval_x' directories inside 'returned_prompts'
    for dir in $(find returned_prompts -type d -name "humaneval_x"); do
        HUMANEVAL_X_PATHS+=("$dir")
    done
    
    # Add additional fixed paths if necessary
    HUMANEVAL_X_PATHS+=("results/humaneval_x" "benchmarks/codefuse-evaluation/codefuseEval/result/")
}

# Function to search for 'cyberseceval' subdirectories
find_cyberseceval_paths() {
    CYBERSECEVAL_PATHS=()
    
    # Find all 'cyberseceval' directories inside 'returned_prompts'
    for dir in $(find returned_prompts -type d -name "cyberseceval"); do
        CYBERSECEVAL_PATHS+=("$dir")
    done
    
    # Add additional fixed paths if necessary
    CYBERSECEVAL_PATHS+=("results/cyberseceval" "benchmarks/PurpleLlama/CybersecurityBenchmarks/results/")
}

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
        case "$2" in
            mbpp)
                find_mbpp_paths
                PATHS=("${MBPP_PATHS[@]}")
                ;;
            humaneval_x)
                find_humaneval_x_paths
                PATHS=("${HUMANEVAL_X_PATHS[@]}")
                ;;
            cyberseceval)
                find_cyberseceval_paths
                PATHS=("${CYBERSECEVAL_PATHS[@]}")
                ;;
            *)
                PATHS=("${DEFAULT_PATHS[@]}")
                ;;
        esac
        compress
        ;;
    decompress)
        decompress
        ;;
    *)
        echo "Usage: $0 {compress|decompress} [mbpp|humaneval_x|cyberseceval]"
        exit 1
        ;;
esac
