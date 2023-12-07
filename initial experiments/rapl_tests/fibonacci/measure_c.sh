#!/bin/bash

NTIMES=200

echo "Language,Program,Package,Core,GPU,DRAM,Time" > measurements_raplc.csv

# Build RAPL
cd RAPL/
make
cd ..

# Function to execute and append measurements to CSV
measure_and_append() {
    PROGRAM=$1
    LANGUAGE=$2
    CSV_LABEL=$3

    sudo ./RAPL/main "$PROGRAM" $NTIMES
    tail -n +2 -q "$PROGRAM.J" | sed "s/^/$LANGUAGE,$CSV_LABEL,/" >> measurements_raplc.csv
}

# Build and measure C programs
gcc -O2 -o fibonacci fibonacci.c
#                  executable |Lang| CSV_label
measure_and_append "fibonacci" "C" "fibonacci"

# Measure Python programs
chmod +x fibonacci.py
#                  executable      |Lang|   CSV_label
measure_and_append "fibonacci.py" "Python" "fibonacci"

# Clean up
cd RAPL/
make clean
cd ..

# Remove temporary files
sudo rm *.J fibonacci
