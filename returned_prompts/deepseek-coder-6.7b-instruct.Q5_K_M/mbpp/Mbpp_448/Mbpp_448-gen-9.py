"""
def cal_sum(n):
    if n<=0:
        return "Input should be positive integer."
    elif n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 2
    else:
        perrin = [0, 1, 2]
        for i in range(3, n):
            perrin.append(perrin[i-1] + perrin[i-2])
        return sum(perrin)
print(cal_sum(9))
"""

Output:
49
"""
"""

