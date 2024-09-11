from functools import reduce
def find_remainder(arr,mod):
    return reduce(lambda x,y: (x*y)%mod, arr)

# assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==