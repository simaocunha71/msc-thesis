
    def count_nums(arr):
        def sum_digits(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        return sum(sum_digits(i) > 0 for i in arr)

    print(count_nums([]))  # 0
    print(count_nums([-1, 11, -11]))  # 1
    print(count_nums([1, 1, 2]))  # 3

"""

def count_nums(arr):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    return sum(sum_digits(i) > 0 for i in arr)

print(count_nums([]))  # 0
print(count_nums([-1, 11, -11]))  # 1
print(count_nums([1, 1, 2]))  # 3
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

#main.py
import os
import sys
import subprocess
import webbrowser
from pathlib import Path

from config import Config
from utils import *

def main():
    config = Config()
    try:
        # Check if the directory exists
        os.chdir(config.dir)
    except FileNotFoundError:
        print(f"Directory {config.dir} not found.")
        sys.exit(1)

    while True:
        print_menu()
        command = input("> ")
        if command == "q":
            break
        elif command == "ls":
            print_files_in_dir()
        elif command == "cd":
            change_dir()
        elif command.startswith("open"):
            open_file(command.split()[1])
        elif command == "mkdir":
            make_dir()
        elif command == "rm":
            remove_