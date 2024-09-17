def next_Perfect_Square(n):
    num = (int)(n**0.5)
    if(num * num != n):
        num += 1
    while(num * num <= n):
        num += 1
    return num*num