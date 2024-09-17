def get_Inv_Count(a):
    result = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                result += 1
    return result