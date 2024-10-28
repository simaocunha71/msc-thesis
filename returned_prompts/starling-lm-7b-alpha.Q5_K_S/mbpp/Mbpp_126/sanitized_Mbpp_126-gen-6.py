def sum(x,y):
    common_divisors = []
    for i in range(1,min(x,y)+1):
        if(x%i == 0 and y%i == 0):
            common_divisors.append(i)
    return sum(common_divisors)