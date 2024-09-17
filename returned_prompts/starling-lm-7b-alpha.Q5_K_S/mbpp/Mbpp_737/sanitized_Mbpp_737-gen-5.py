from typing import Union
def check_str(s: Union[str, None]) -> bool:
    """
    Check if string starts with a vowel using regex
    """
    if s is None:
        return False
    return s.startswith(r"[aeiouAEIOU]")