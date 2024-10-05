
import re

class Solution:
    def count_distinct_characters(self, string: str) -> int:
        return len(set(re.split(r'[^a-zA-Z]+', string)))
