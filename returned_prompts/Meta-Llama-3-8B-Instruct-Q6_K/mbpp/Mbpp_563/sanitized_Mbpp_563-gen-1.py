def extract_values(s):
    return [value.strip('"') for value in s.split('"') if value.strip('"')]  # extract values between quotation marks from a string