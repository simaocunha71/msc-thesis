
def get_ludic(n):
    ludic = []
    for i in range(1, n+1):
        if i == 1 or i%2 != 0 and all(i%j != 0 for j in range(2, int(i**0.5)+1)):
            ludic.append(i)
    return ludic


