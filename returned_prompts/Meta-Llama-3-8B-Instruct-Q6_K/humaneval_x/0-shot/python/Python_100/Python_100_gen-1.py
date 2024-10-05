    def make_a_pile(n):
        result = []
        for i in range(n):
            if i % 2 == 0:
                result.append(i*2 + 1)
            else:
                result.append(i*2 + 2)
        return result
    # test the function
    print(make_a_pile(3))  # [3, 5, 7]
    print(make_a_pile(5))  # [5, 6, 9, 10, 11]
    print(make_a_pile(8))  # [8, 10, 12, 14, 16, 18, 20, 22]
    print(make_a_pile(10))  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    print(make_a_pile(15))  # [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]
    print(make_a_pile(20))  # [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    print(make_a_pile(25))  # [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50]




def make_a_pile(n):
    result = []
    odd = 1
    even = 2
    for i in range(n):
        if i % 2 == 0:
            result.append(even)
            even += 2
        else:
            result.append(odd)
            odd += 2
    return result

print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(5))  # [5, 6, 9, 10, 11]
print(make_a_pile(8))  # [