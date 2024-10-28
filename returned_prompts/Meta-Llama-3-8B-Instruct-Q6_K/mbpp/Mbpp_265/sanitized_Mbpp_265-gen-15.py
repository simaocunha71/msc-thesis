def list_split(lst, n):
    result = []
    i = 0
    while i < len(lst):
        result.append(lst[i:i+n])
        i += n
    return result