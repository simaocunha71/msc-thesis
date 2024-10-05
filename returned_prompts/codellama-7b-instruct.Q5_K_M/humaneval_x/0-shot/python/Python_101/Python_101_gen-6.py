
import re

def words_string(s):
    return re.findall(r'[a-zA-Z]+', s)
