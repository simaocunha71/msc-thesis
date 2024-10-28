from collections import Counter
from collections import defaultdict
def first_repeated_char(s:str)->str:
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]]>1 and s.index(s[i])!=i:
            return s[i]
    return "No repeated char"