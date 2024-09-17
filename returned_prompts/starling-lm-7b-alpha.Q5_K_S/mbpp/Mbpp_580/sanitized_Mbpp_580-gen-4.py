from collections import deque
from collections import Counter
import sys
def extract_even(t):
    even = []
    for elem in t:
        if isinstance(elem, tuple):
            even.append(extract_even(elem))
        else:
            if elem % 2 == 0:
                even.append(elem)
    return even