import sys, os, time, csv
import pyRAPL
import subprocess

def start_measure():
    NTIMES = 20

    subprocess.run("sudo chmod -R a+r /sys/class/powercap/intel-rapl", shell=True)

    pyRAPL.setup()

    for _ in range(NTIMES+1):
        subprocess.run(["gcc", "-O2", "-o", "fibonacci", "fibonacci.c"])

        start_time = time.time()
        measure = pyRAPL.Measurement('fibonacci_c')
        measure.begin()
        subprocess.run(["./fibonacci"])
        measure.end()
        end_time = time.time()
        execution_time = end_time - start_time
        with open(FILENAME, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["C", "fibonacci", execution_time, measure.result.pkg[0], measure.result.dram[0]])

    for _ in range(NTIMES+1):
        subprocess.run(["chmod", "+x", "fibonacci.py"])

        start_time = time.time()
        measure = pyRAPL.Measurement('fibonacci_python')
        measure.begin()
        subprocess.run(["./fibonacci.py"])
        measure.end()
        end_time = time.time()
        execution_time = end_time - start_time
        with open(FILENAME, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Python", "fibonacci", execution_time, measure.result.pkg[0], measure.result.dram[0]])

if __name__ == "__main__":

    FILENAME = "measurements_pyrapl.csv"

    subprocess.run("sudo chmod -R a+r /sys/class/powercap/intel-rapl", shell=True)

    # List with the values of the csv's header
    header_list = [
                   "Language",
                   "Program",
                   "Execution time",
                   "Package",
                   "DRAM"
                  ]

    if not os.path.isfile(FILENAME) or os.stat(FILENAME).st_size == 0:
        # If file doesn't exists, it will be created
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    start_measure()

















































"""
Descrição das colunas CSV:

label (str) - measurement label
timestamp (float) - measurement's beginning time (expressed in seconds since the epoch)
duration (float) - measurement's duration (in micro seconds)
pkg (Optional[List[float]]) - list of the CPU energy consumption -expressed in micro Joules- (one value for each socket) if None, no CPU energy consumption was recorded
dram (Optional[List[float]]) - list of the RAM energy consumption -expressed in seconds- (one value for each socket) if None, no RAM energy consumption was recorded
"""
