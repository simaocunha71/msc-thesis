def choose_num(x,y):
    x += 1
    if x % 2 == 0:
        return x
    else:
        x += 1
        if x % 2 == 0:
            return x
        else:
            x += 1
            if x % 2 == 0:
                return x
            else:
                return -1

B:
def choose_num(x,y):
    for i in range(x,y+1):
        if i % 2 == 0:
            return i
        else:
            continue
    return -1

C:
def choose_num(x,y):
    for i in range(x,y+1):
        if i % 2 == 0:
            return i
    return -1
根据上面的代码片段，下面哪段代码是正确的，哪段代码是错误的？
