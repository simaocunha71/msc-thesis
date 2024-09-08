def test_three_equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0

print(test_three_equal(1,1,1))  # 3
print(test_three_equal(1,2,1))  # 2
print(test_three_equal(1,2,3))  # 0
print(test_three_equal(1,1,2))  # 2
print(test_three_equal(2,2,2))  # 3
print(test_three_equal(1,2,2))  # 2
print(test_three_equal(1,1,2))  # 2
print(test_three_equal(1,2,1))  # 2
print(test_three_equal(2,2,1))  # 2
print(test_three_equal(2,1,1))  # 2
print(test_three_equal(1,1,1))  # 3
print(test_three_equal(1,2,3))  # 0
print(test_three_equal(2,2,3))  # 2
print(test_three_equal(2,3,3))  # 3
print(test_three_equal(3,3,3))  # 3
print(test_three_equal(1,2,2))  # 2
print(test_three_equal(2,2,2))  # 3
print(test_three_equal(2,1,1))  # 2
print(test_three_equal(2,2,1))  # 2
print(test_three_equal(2,1,2))  # 2
print(test_three_equal(1,2,1))  # 2
print(test_three_equal(2,2,2))  # 3
print(test_three_equal(2,2,3))  # 2
print(test_three_equal(2,3,3))  # 