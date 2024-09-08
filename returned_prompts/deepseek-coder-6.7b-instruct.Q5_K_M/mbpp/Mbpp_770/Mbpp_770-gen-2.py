def odd_num_sum(n):
    sum = 0
    for i in range(n):
        sum += (2*i + 1)**4
    return sum


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum((2*i + 1)**4 for i in range(n))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n, 2))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum((2*i + 1)**4 for i in range(n))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum(map(lambda x: x**4, (2*i + 1 for i in range(n))))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum(map(lambda x: x**4, range(1, 2*n, 2)))


print(odd_num_sum(2))  # 82


# OR

def odd_num_sum(n):
    return sum(map(lambda x: x**4, [i for i in range(1, 2*n, 2)]))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum((2*i + 1)**4 for i in range(n))


print(odd_num_sum(2))  # 82

# OR

def odd_num_sum(n):
    return sum((2*i + 1)**4 for i in range(n))


print(odd_num_sum(2))  # 82