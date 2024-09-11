import re
from functools import reduce
def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])  # Convert string to list of characters, filter out lowercase characters and join back to string