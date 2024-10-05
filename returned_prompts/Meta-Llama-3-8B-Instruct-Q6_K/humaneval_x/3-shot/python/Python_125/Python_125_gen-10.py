    words = txt.split()
    if not words and ',' in txt:
        return txt.replace(',', '').lower().count('a') // 2 + 1
    return words


