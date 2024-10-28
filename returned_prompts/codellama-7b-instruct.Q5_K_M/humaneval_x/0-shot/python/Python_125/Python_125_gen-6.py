
    import re
    
    txt = txt.strip()
    if re.search(r'\s', txt):
        return txt.split()
    else:
        return sum([1 for c in txt if ord(c) % 2])



