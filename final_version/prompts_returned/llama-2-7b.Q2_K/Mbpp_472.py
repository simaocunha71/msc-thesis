"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
from typing import Any, Dict, List, Optional, Set, Type, Union # pylint: disable=line-too-long

import math
# pylint: disable=unnecessary-lambda, pointless-statement-with-empty-block, too-many-locals, no-self-use, unused-argument
def check_Consecutive(a: List[float]) -> bool:  # pylint: disable=invalid-name
    assert type(a) is list and len(a) > 0 and all(x in xrange for x in a), "The list contains no numbers"
    
    def check_sequence(n: int, seq: List[float]) -> bool:
        assert math.isnan(n) == False, 'Nan is not allowed here'
        
        if n > 0 and n < len(seq):
            return all([check_Consecutive(next(seq)) for next in seq[:n]])
        else:
            return math.isnan(n) or any([math.isnan(i) for i, x in enumerate(a[::-1]) if not check_Consecutive(x)] < len(a[::-1]))
    n = float(- 1)
    
    for elm in a:  # pylint: disable=unnecessary-lambda, pointless-statement-with-empty-block, too-many-locals, no-self-use, unused-argument
        check_sequence(n+1, [elm])
    
    return n == math.nan or check_sequence(0, a)
