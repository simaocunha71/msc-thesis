
import re

def is_bored(S):
    return len(re.findall(r"I\b", S))
