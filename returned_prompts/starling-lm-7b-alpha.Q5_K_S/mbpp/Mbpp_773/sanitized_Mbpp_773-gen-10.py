def occurance_substring(main_str, sub_str):
    i = main_str.find(sub_str)
    if i == -1:
        return None
    else:
        return (sub_str, i, i + len(sub_str))