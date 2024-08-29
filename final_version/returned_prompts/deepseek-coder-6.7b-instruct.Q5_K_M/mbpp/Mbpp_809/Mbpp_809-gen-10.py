def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t1[i] >= t2[i]:
            return False
    return True

print(check_smaller((1, 2, 3), (2, 3, 4)))

