def extract_values(s):
    return [i.strip('"') for i in s.split('"') if i]