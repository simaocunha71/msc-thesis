
def occurance_substring(string, sub):
    index = string.find(sub)
    if index == -1:
        return None
    else:
        length = len(sub)
        return (sub, index, index + length)


