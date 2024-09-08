def last(lst, num):
    try:
        return len(lst) - 1 - lst[::-1].index(num)
    except ValueError:
        return -1