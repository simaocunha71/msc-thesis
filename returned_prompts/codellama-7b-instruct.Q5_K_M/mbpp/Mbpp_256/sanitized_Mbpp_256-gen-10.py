def count_Primes_nums(n):
    if n<2:
        return 0
    prime_nums = [2]
    for i in range(3,n+1,2):
        flag = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            prime_nums.append(i)
    return len(prime_nums)