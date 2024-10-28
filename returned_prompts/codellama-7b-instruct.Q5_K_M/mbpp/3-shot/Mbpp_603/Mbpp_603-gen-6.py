
def get_lucid(limit):
    ludic = [1, 2]
    for i in range(2, limit + 1):
        if i % ludic[-1] != 0:
            ludic.append(i)
        else:
            continue
    return ludic


