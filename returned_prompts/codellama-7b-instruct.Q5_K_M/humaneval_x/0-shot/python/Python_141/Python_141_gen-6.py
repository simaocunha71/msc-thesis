
import re

def file_name_check(file_name):
    pattern = re.compile("^[a-zA-Z][a-zA-Z0-9]{0,2}\.[txt|exe|dll]$")
    if pattern.match(file_name):
        return 'Yes'
    return 'No'

# 2
