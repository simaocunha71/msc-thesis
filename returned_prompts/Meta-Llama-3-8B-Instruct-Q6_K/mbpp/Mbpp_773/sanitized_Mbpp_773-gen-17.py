def occurance_substring(s, sub_str):
    try:
        pos = s.index(sub_str)
        return (sub_str, pos, pos + len(sub_str) - 1)
    except ValueError:
        return None