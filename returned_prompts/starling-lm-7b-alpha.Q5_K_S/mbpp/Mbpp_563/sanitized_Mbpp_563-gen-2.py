def extract_values(s):
    s = s.replace("\"", "")
    return [i for i in s.split(",")]