import re

def check_str(s):
    return bool(re.match('^[aeiou]', s, re.I))

print(check_srt("annie"))

# 10. Write a Python function to find the maximum and minimum number from a list of numbers.
