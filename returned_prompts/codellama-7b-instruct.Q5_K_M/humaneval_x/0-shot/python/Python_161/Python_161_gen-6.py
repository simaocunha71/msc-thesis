
import re

def solve(s):
    r = re.sub(r'([a-z])', lambda x: x.group(1).upper(), s)
    r = re.sub(r'([A-Z])', lambda x: x.group(1).lower(), r)
    return r if re.search(r'[a-zA-Z]', r) else r[::-1]
