def extract_values(s):
    return [x.strip('"') for x in s.split('"') if x.strip('"')]