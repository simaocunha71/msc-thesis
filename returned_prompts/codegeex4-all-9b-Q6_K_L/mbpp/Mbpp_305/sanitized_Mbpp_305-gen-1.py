def start_withp(lst):
    result = []
    for word in lst:
        if word.startswith('p'):
            result.append(word)
    return tuple(result[:2]) if len(result) >= 2 else tuple(result)