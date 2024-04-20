"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
from typing import List, Optional

def change_date_format(s: str) -> Optional[str]:
    """
    :param s: Date in yyyy-mm-dd format.
    
    >>> change_date_format("1980-04-27")
    '27-04-1980'
    """
    # your code here
    return 23