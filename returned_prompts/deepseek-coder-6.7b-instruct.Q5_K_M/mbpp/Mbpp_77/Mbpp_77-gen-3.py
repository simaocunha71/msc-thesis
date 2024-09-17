
def is_Diff(num):
    num = str(num)
    if len(num) < 2:
        return False
    else:
        return abs(int(num[0]) - int(num[1])) == 1


