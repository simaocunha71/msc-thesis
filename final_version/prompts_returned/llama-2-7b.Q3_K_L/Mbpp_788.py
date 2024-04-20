"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""
class Solution:
    def new_tuple(self, s: str, t: List[str]) -> Tuple:
        return (s,) + tuple(t)
