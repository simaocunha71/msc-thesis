
def digits(n):
    # Your code goes here
    # 1. 找到所有的单个数字
    # 2. 判断这个数字是不是奇数
    # 3. 如果是奇数，那么就乘以这个数字
    # 4. 如果所有的数字都是偶数，那么就返回0

    single_digits = [int(i) for i in str(n)]
    result = 0
    for i in single_digits:
        if i % 2 == 1:
            result *= i
    return result


