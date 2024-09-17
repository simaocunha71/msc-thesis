def start_withp(my_list):
    for word in my_list:
        if word.split()[0] == 'Python':
            return tuple(word.split())
    return ()