def odd_position(lst):
    return all(i%2!=0 and i%2!=1 for i in lst[1::2])  # checking odd index and odd number