def start_withp(lst):
    words = lst[0].split()
    return tuple(word for word in words if word.startswith('p'))