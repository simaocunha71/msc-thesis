def extract_quotation(s):
    return [i[1:-1] for i in s.split(' ') if i[0]=='"' and i[-1]=='"']