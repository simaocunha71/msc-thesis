
from collections import Counter
import re

def max_run_uppercase(s):
    """
    :type s: str
    :rtype: int
    """
    #return max(map(len, re.split('[^A-Z]', s)))
    return max(map(len, re.findall('[A-Z]+', s)))
