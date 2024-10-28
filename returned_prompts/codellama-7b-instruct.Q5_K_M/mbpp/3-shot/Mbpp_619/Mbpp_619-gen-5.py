
import re
def move_num(s):
    return re.sub(r'\d+', '', s) + re.sub(r'\D', '', s)


