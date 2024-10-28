from collections import Counter
from collections import defaultdict
from collections import defaultdict
from collections import defaultdict
from collections import defaultdict
def unique_sublists(lst):
    return {tuple(sublist): lst.count(tuple(sublist)) for sublist in set(map(tuple, lst))}  # using set to remove duplicates and map to convert lists to tuples