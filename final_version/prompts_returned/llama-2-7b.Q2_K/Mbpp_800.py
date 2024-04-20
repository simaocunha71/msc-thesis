"""
Write a function to remove all whitespaces from a string.
assert remove_all_spaces('python  program')==('pythonprogram')
"""
from typing import Any, Dict, List, Optional, Set, Type, Union, overload

import re

T = Type("T")
t: T = overload(lambda x: x)(T)


def remove_all_spaces(s: str) -> str:  # type: ignore[override]
    return "".join([v for v in s.split() if not v.isspace()])


class Solution20:
    def removeAllSpaces(self, s: str) -> int:  # type: ignore[override]
        return len(re.findall("[\S]+", s))
