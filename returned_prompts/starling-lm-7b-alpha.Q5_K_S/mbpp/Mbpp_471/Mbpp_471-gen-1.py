def find_remainder(arr,n):
    if len(arr) == 1:
        return arr[0] % n
    else:
        if len(arr)%2 == 0:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n)) % n
        else:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n) * arr[-1]) % n


find_remainder([ 100, 10, 5, 25, 35, 14 ],11)




"""
def find_remainder(arr,n):
    if len(arr) == 1:
        return arr[0] % n
    else:
        if len(arr)%2 == 0:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n)) % n
        else:
            return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n) * arr[-1]) % n

find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

# def find_remainder(arr,n):
#     if len(arr) == 1:
#         return arr[0] % n
#     else:
#         if len(arr)%2 == 0:
#             return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n)) % n
#         else:
#             return (find_remainder(arr[:-1],n) * find_remainder(arr[1:],n) * arr[-1]) % n

# find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9












