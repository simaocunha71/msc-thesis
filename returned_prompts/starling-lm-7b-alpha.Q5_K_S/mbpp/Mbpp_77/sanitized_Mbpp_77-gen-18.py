def is_Diff(num):
    return abs(sum(map(int, str(num))) - (sum(map(int, str(num))) % 11)) == 11