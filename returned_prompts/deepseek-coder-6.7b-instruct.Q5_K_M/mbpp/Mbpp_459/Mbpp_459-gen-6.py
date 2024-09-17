
import re
def remove_uppercase(s):
    return re.sub(r'[A-Z]+', '', s)


