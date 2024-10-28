def number_ctr(s):
    return s.count(str(int(max(map(int, [i for i in s if i.isdigit()]))))) if any(i.isdigit() for i in s) else 0