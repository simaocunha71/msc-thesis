    l.sort()
    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue
        l_ptr, r_ptr = i+1, len(l)-1
        while l_ptr < r_ptr:
            s = l[i] + l[l_ptr] + l[r_ptr]
            if s < 0:
                l_ptr += 1
            elif s > 0:
                r_ptr -= 1
            else:
                return True
    return False


