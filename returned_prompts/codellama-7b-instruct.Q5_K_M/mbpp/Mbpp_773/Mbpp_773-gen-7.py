def occurance_substring(string, sub_string):
    if sub_string in string:
        return (sub_string, string.index(sub_string), string.index(sub_string)+len(sub_string))
    else:
        return None


