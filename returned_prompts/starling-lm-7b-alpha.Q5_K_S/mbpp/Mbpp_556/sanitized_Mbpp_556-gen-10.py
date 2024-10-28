def find_Odd_Pair(a,b):
    #counting odd and even number of pairs
    odd_count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]^a[j])%2 != 0:
                odd_count += 1
    return odd_count