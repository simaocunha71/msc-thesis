#!/bin/bash

# Default ZIP file name for compression (not decompression)
ZIP_FILE=${3:-"mbpp_results.zip"}

# Default list of paths
DEFAULT_PATHS=(
    "returned_prompts/"
    "results/"
    "benchmarks/evalplus/results/"
    "benchmarks/codefuse-evaluation/codefuseEval/result/"
    "benchmarks/PurpleLlama/CybersecurityBenchmarks/results/"
)

# Enable verbose output if set
VERBOSE=${VERBOSE:-0}

# Function to log verbose messages
log() {
    if [ "$VERBOSE" -eq 1 ]; then
        echo "$@"
    fi
}

# Function to search for 'mbpp' subdirectories
find_mbpp_paths() {
    MBPP_PATHS=()
    
    # Find all 'mbpp' directories inside 'returned_prompts'
    for dir in $(find returned_prompts -type d -name "mbpp"); do
        log "Found mbpp directory: $dir"
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
        log "Found humaneval_x directory: $dir"
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
        log "Found cyberseceval directory: $dir"
        CYBERSECEVAL_PATHS+=("$dir")
    done
    
    # Add additional fixed paths if necessary
    CYBERSECEVAL_PATHS+=("results/cyberseceval" "benchmarks/PurpleLlama/CybersecurityBenchmarks/results/")
}

# Function to find paths for all benchmarks (mbpp, humaneval_x, cyberseceval)
find_all_paths() {
    find_mbpp_paths
    find_humaneval_x_paths
    find_cyberseceval_paths
    
    # Merge all benchmark paths into one array
    ALL_PATHS=("${MBPP_PATHS[@]}" "${HUMANEVAL_X_PATHS[@]}" "${CYBERSECEVAL_PATHS[@]}")
}

# Function to check if a directory exists before adding to PATHS
check_directories_exist() {
    local dirs=("$@")
    local valid_dirs=()

    for dir in "${dirs[@]}"; do
        if [ -d "$dir" ]; then
            log "Directory exists: $dir"
            valid_dirs+=("$dir")
        else
            log "Warning: Directory $dir does not exist."
        fi
    done

    PATHS=("${valid_dirs[@]}")
}

# Function to compress files into a ZIP archive
compress() {
    echo "Moving files to $ZIP_FILE..."

    # Move the directories into the ZIP file
    zip -rm "$ZIP_FILE" "${PATHS[@]}"
    
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
    local zip_file="$2"

    # Check if the ZIP file was provided as an argument
    if [ -z "$zip_file" ]; then
        echo "Error: No ZIP file provided for decompression!"
        echo "Usage: $0 decompress <zip_file_path>"
        exit 1
    fi

    # Check if the ZIP file exists
    if [ ! -f "$zip_file" ]; then
        echo "ZIP file $zip_file not found!"
        exit 1
    fi

    echo "Restoring files from $zip_file..."

    # Extract the ZIP file into a temporary folder
    unzip -o "$zip_file" -d ./extracted_files
    
    # Iterate through the extracted files
    for file in ./extracted_files/*; do
        if [ -d "$file" ]; then
            folder_name=$(basename "$file")
            if [ -d "$folder_name" ]; then
                echo "Directory $folder_name exists. Merging contents."
                cp -R "$file"/* "$folder_name"/
            else
                echo "Moving $folder_name to the current directory."
                mv "$file" .
            fi
        fi
    done
    
    rm -rf ./extracted_files
    
    # Check if the operation was successful
    if [ $? -eq 0 ]; then
        echo "Files restored successfully!"
        
        # Delete the ZIP file after successful decompression
        echo "Deleting ZIP file: $zip_file"
        rm "$zip_file"
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
                check_directories_exist "${MBPP_PATHS[@]}"
                ;;
            humaneval_x)
                find_humaneval_x_paths
                check_directories_exist "${HUMANEVAL_X_PATHS[@]}"
                ;;
            cyberseceval)
                find_cyberseceval_paths
                check_directories_exist "${CYBERSECEVAL_PATHS[@]}"
                ;;
            all)
                find_all_paths
                check_directories_exist "${ALL_PATHS[@]}"
                ;;
            *)
                check_directories_exist "${DEFAULT_PATHS[@]}"
                ;;
        esac
        compress
        ;;
    decompress)
        decompress "$@"
        ;;
    *)
        echo "Usage: $0 {compress|decompress} [mbpp|humaneval_x|cyberseceval|all] [zip_filename]"
        exit 1
        ;;
esac
