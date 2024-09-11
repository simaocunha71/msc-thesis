def number_ctr(s):
    return s.count(str(int(''.join(filter(str.isdigit, s)))))