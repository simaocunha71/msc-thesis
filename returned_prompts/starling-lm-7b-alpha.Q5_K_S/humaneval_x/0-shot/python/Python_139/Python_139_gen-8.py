
def special_factorial(n):
    if n == 0:
        return 1
    else:
        return n * special_factorial(n-1)


# Test cases
print(special_factorial(0))  # 1
print(special_factorial(1))  # 1
print(special_factorial(2))  # 2
print(special_factorial(3))  # 6
print(special_factorial(4))  # 24
print(special_factorial(5))  # 120
print(special_factorial(6))  # 720
print(special_factorial(7))  # 5040
print(special_factorial(8))  # 40320


# More test cases
print(special_factorial(10))  # 3628800
print(special_factorial(11))  # 39916800
print(special_factorial(12))  # 35568742400
print(special_factorial(13))  # 3048879628800
print(special_factorial(14))  # 2363687887033600
print(special_factorial(15))  # 18157007924094752000
print(special_factorial(16))  # 13516161584099876160000
print(special_factorial(17))  # 101133731096734019200032000
print(special_factorial(18))  # 7581861295738053760025600000
print(special_factorial(19))  # 5707295908304137952020160000