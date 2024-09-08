def start_withp(lst):
    result = []
    for item in lst:
        words = item.split()
        for word in words:
            if word.lower().startswith('p'):
                result.append(word)
    return tuple(result)