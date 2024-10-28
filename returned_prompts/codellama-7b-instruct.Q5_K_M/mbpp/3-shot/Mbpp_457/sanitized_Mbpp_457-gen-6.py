def Find_Min(sublist):
    if sublist == []:
        return None
    return min(sublist, key=len)