from functools import reduce
def find_remainder(arr,mod):
    return reduce(lambda x,y: (x*y)%mod, arr)