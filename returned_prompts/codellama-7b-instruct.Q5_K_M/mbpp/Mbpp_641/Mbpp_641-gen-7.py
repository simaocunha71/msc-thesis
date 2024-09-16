def is_nonagonal(n):
    return ((n*n)**(1/2))%2 == 0

def find_nth_nonagonal(n):
    i = 1
    while is_nonagonal(i) == False:
        i += 1
    return i

def is_nonagonal(n):
    return ((n*n)**(1/2))%2 == 0
