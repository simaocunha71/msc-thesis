def extract_quotation(s):
    return [word for word in s.split() if word.startswith('"') and word.endswith('"')][1:-1].split('"')[1::2]  # [1:-1] to remove the first and the last word, [1::2] to get all the words between the first and the last