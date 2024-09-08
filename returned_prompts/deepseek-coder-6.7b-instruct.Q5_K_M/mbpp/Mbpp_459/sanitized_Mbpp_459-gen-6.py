import re
def remove_uppercase(s):
    output = ""
    for word in s.split(" "):
        if not word.isupper():
            output += word + " "
    return output.strip()