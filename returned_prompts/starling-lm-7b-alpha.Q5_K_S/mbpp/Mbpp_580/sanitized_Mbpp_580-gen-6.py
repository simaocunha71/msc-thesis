def extract_even(tup):
    for i in range(len(tup)):
        if isinstance(tup[i], tuple):
            tup[i] = extract_even(tup[i])
        elif isinstance(tup[i], list):
            tup[i] = [j for j in tup[i] if j%2==0]
        elif tup[i]%2!=0:
            tup.remove(tup[i])
    return tuple(tup)