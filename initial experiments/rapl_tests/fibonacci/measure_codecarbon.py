import sys, os, time, csv
from codecarbon import OfflineEmissionsTracker, track_emissions
import subprocess

def convert_kwh_to_j(value):
    return value * (3.6*(10**6))

def start_measure():
    NTIMES = 200

    for _ in range(NTIMES):
        os.system("gcc -O2 -o fibonacci fibonacci.c")

        tracker = OfflineEmissionsTracker(country_iso_code="PRT")
        tracker.start()
        os.system("./fibonacci")
        tracker.stop()

        with open(FILENAME, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            try:
                csv_writer.writerow(["C", "fibonacci", 
                                          tracker.final_emissions_data.duration, 
                                          convert_kwh_to_j(tracker.final_emissions_data.cpu_energy), 
                                          convert_kwh_to_j(tracker.final_emissions_data.ram_energy), 
                                          convert_kwh_to_j(tracker.final_emissions_data.gpu_energy),  
                                          tracker.final_emissions_data.cpu_power, 
                                          tracker.final_emissions_data.ram_power,  
                                          tracker.final_emissions_data.gpu_power, 
                                          tracker.final_emissions_data.emissions,
                                          tracker.final_emissions_data.emissions_rate
                                    ])
            except Exception as e:
                print("------------------------------------------")
                print(e)
                print("------------------------------------------")

                csv_writer.writerow(["C", "fibonacci", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR",
                                                                       "ERROR", "ERROR", "ERROR", "ERROR"
                                    ])
        time.sleep(5)
        
    for _ in range(NTIMES):
        os.system("chmod +x fibonacci.py")

        tracker = OfflineEmissionsTracker(country_iso_code="PRT")
        tracker.start()
        os.system("./fibonacci.py")
        tracker.stop()

        with open(FILENAME, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            try:
                csv_writer.writerow(["Python", "fibonacci", 
                                          tracker.final_emissions_data.duration, 
                                          convert_kwh_to_j(tracker.final_emissions_data.cpu_energy), 
                                          convert_kwh_to_j(tracker.final_emissions_data.ram_energy), 
                                          convert_kwh_to_j(tracker.final_emissions_data.gpu_energy),  
                                          tracker.final_emissions_data.cpu_power, 
                                          tracker.final_emissions_data.ram_power,  
                                          tracker.final_emissions_data.gpu_power, 
                                          tracker.final_emissions_data.emissions,
                                          tracker.final_emissions_data.emissions_rate
                                    ])
            except Exception as e:
                print("------------------------------------------")
                print(e)
                print("------------------------------------------")

                csv_writer.writerow(["C", "fibonacci", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR",
                                                                       "ERROR", "ERROR", "ERROR", "ERROR"
                                    ])
        time.sleep(5)


if __name__ == "__main__":

    FILENAME = "measurements_codecarbon.csv"

    # List with the values of the csv's header
    header_list = [
                   "Language",
                   "Program",
                   "Execution time (s)",
                   "CPU Energy (J)",
                   "RAM Energy (J)",
                   "GPU Energy (J)",
                   "CPU Power (W)", 
                   "RAM Power (W)",
                   "GPU Power (W)",
                   "CO2 emissions (Kg)",
                   "CO2 emissions rate (Kg/s)"
                  ]

    if not os.path.isfile(FILENAME) or os.stat(FILENAME).st_size == 0:
        # If file doesn't exists, it will be created
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header_list)

    start_measure()
    os.remove("emissions.csv")