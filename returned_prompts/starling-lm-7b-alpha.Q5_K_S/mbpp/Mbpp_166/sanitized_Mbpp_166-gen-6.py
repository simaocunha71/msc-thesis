def find_even_pair(L):
    c = 0
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            if (L[i]^L[j])%2 == 0:
                c += 1
    return c