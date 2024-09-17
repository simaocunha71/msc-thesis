def is_Monotonic(a):
    inc = True
    dec = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            dec = False
        elif a[i] < a[i+1]:
            inc = False
    if inc == True or dec == True:
        return True
    else:
        return False