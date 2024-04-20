"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
from typing import Any, Dict, List, Optional, Set, Type, Union # noqa: EPE1Spy,EPE11y
from io import StringIO # isort:skip
import sys
# exception_types = [TypeError]
# class_declaration = """def return_count(x, y):"""
# class_body = """\treturn find_Odd_Pair(set([x]), y)"""
# def function(*args: Any) -> None: # noqa: E501
# 	print(''.join(['F', str(arg), ']' for arg in args]))
# if __name__ == "__main__":
# 	function(x=5, y=4, z=7, a=2, b=-1)
def find_Odd_Pair(
    *,
    x: Union[int, int, str] = 0,
    y: Optional[Union[int, Set[int]]] = None,
):
    from collections import Counter as CT # noqa: EPE1Spy
    if type(x) not in (str, int): x, y = [x, y]
    cnt_odd = CT()
    try:
        while True:
            try:
                assert isinstance(y, set) and len(set(x)) == 2
                if type(y) not in (list, set): y = list(y)
            except AssertionError as e:
                print("AssertionError:", str(e), "\n")
                break
    finally:
        return cnt_odd.most_common()[-2][0]
