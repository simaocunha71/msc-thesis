def merge_sorted_list(a, b, c):
    result = []
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] < b[j]:
            if a[i] < c[k]:
                result.append(a[i])
                i += 1
            else:
                result.append(c[k])
                k += 1
        else:
            if b[j] < c[k]:
                result.append(b[j])
                j += 1
            else:
                result.append(c[k])
                k += 1
    result += a[i:] + b[j:] + c[k:]
    return result