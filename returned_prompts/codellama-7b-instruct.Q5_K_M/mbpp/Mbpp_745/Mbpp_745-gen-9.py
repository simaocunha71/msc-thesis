
def divisible_by_digits(startnum, endnum):
    ans = []
    for num in range(startnum, endnum + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                ans.append(num)
                break
    return ans


