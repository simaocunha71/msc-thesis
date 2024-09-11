from typing import Set
import re
def find_char_long(s: str) -> Set[str]:
    return set(word for word in re.findall(r'\b\w+\b', s) if len(word) >= 4)  # using regular expression to find all words in the string and then filter the ones with length greater than or equal to 4