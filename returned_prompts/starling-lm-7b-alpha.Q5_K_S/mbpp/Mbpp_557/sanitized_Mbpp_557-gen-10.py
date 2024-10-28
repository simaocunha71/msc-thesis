def toggle_string(s):
    l = list(s)
    for i in range(len(s)):
        if l[i].isupper():
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return "".join(l)