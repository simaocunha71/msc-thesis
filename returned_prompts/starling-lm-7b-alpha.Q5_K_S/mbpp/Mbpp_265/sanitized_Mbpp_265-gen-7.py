def list_split(lst, n):
    output = []
    while lst:
        output.append(lst[:n])
        lst = lst[n:]
    return output