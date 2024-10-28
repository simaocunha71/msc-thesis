def get_ludic(num):
    ludics = []
    for i in range(1, num+1):
        if i % 2 != 0 and i % 5 != 0:
            ludics.append(i)
    return ludics