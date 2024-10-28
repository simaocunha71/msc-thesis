def occurance_substring(string, sub_string):
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            return (sub_string, i, i+len(sub_string))
    return None