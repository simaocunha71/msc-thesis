def pair_wise(my_list):
    pairs = []
    for i in range(len(my_list)-1):
        pairs.append((my_list[i], my_list[i+1]))
    return pairs

# test
my_list = [1,1,2,3,3,4,4,5]
print(pair_wise(my_list))

# [[1, 1], [1, 2], [2, 3], [3, 3], [3, 4], [4, 4], [4, 5]]

