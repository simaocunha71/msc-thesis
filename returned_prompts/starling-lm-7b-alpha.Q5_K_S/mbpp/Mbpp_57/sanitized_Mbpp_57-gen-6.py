from itertools import permutations
def find_Max_Num(lis):
    perm = permutations(lis)
    max = 0
    for i in perm:
        i = int("".join(map(str,i)))
        if i > max:
            max = i
    return max
lis = [1, 2, 3]