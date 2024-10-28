def occurance_substring(s: str, sub_str: str) -> tuple:
    try:
        start = s.index(sub_str)
        return (sub_str, start, start + len(sub_str))
    except ValueError:
        return None