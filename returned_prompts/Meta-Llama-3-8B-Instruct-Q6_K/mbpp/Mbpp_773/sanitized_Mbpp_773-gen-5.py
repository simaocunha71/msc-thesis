def occurance_substring(s: str, sub_str: str) -> tuple:
    if sub_str in s:
        return (sub_str, s.index(sub_str), len(sub_str))
    else:
        return None