def extract_values(s):
    return [value.strip('"') for value in s.split('"') if value.strip('"')]