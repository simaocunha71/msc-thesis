
def is_Diff(n):
    return abs(sum(map(int,str(n))) - (int(str(n)[0]) + int(str(n)[-1]))) % 11 == 0


