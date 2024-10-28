def dif_Square(n):
    i=1
    while i*i <= n:
        if n%i == 0 and (n//i) - i == i:
            return True
        i+=1
    return False

