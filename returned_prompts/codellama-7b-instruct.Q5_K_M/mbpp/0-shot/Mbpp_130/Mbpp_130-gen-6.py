
# %%
from collections import Counter
from typing import List

def max_occurrences(my_list: List) -> int:
    counter = Counter(my_list)
    return counter.most_common()[0][0]

# %%
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2

# %%
