from itertools import product
def maximize_elements(t1, t2):
    max_t = [max(x, y) for x, y in zip(t1, t2)]
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == max_t[i] and t2[j] == max_t[j]:
                continue
            if t1[i] == max_t[j] and t2[j] == max_t[i]:
                max_t[i], max_t[j] = max_t[j], max_t[i]
    return max_t