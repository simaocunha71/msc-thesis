def digit_distance_nums(n1,n2):
    l1 = list(str(n1))
    l2 = list(str(n2))
    if len(l1)!=len(l2):
        return None
    else:
        return sum(abs(int(l1[i])-int(l2[i])) for i in range(len(l1)))