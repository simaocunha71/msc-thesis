def odd_Equivalent(bin_str, rot):
    bin_str = bin_str * rot
    count = 0
    for i in range(rot):
        temp = bin_str[i: len(bin_str) ] + bin_str[0: i]
        if temp.count('1') % 2 != 0:
            count += 1
    return count