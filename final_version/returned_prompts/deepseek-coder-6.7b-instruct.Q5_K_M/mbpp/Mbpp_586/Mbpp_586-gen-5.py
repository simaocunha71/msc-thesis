def split_Arr(arr, n):
    return arr[n:] + arr[:n]

assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""

