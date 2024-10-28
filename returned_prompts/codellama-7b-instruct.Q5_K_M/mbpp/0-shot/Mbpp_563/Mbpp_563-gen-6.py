def extract_values(s):
    return [value for value in s.split(',') if value.startswith('"') and value.endswith('"')]

