def occurance_substring(s, sub_str):
    if sub_str in s:
        return sub_str, s.index(sub_str), s.index(sub_str) + len(sub_str)
    else:
        return None
    # if s.find(sub_str) != -1:
    #     return sub_str, s.find(sub_str), s.find(sub_str) + len(sub_str)
    # else:
    #     return None