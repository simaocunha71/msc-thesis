def find_Odd_Pair(lst,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if bin(lst[i]^lst[j]).count('1')%2!=0:
                count+=1
    return count