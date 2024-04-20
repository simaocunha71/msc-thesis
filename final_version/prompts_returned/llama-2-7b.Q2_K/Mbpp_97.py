"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.
assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]])=={1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""
import collections
from typing import List

def frequency_lists(myLists) -> dict:
    """Return a dictionary of the frequency of elements in the lists."""
    
    # Create a dictionary mapping each list element to its frequency.
    freqDict = collections.defaultdict(int)
    
    for lst in myLists:
        for item in lst:
            freqDict[item] += 1
            
    return freqDict
