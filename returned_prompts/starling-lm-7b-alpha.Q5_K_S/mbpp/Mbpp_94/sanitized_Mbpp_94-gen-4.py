def index_minimum(t):
    minimum = t[0][1]
    for i in range(1, len(t)):
        if t[i][1] < minimum:
            minimum = t[i][1]
            index = i
    return t[index][0]