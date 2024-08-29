def list_split(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

