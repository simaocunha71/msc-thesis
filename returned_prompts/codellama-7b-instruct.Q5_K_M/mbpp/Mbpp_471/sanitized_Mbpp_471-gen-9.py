def find_remainder(arr,n):
    return reduce((lambda x,y: (x*y)%n),arr,1)