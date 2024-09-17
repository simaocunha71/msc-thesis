
import re
def extract_values(my_string):
    return re.findall(r'"([^"]*)"', my_string)


