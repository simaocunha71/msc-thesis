def extract_values(s):
    return [item for item in s.split(',') if item.startswith('"') and item.endswith('"')]