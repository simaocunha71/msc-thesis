
def check(num):
    reversed_num = int(str(num)[::-1])
    if (num == reversed_num + 1):
        return True
    else:
        return False


