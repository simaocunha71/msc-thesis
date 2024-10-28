
def choose_num(x, y):
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    return -1


# Test cases
print(choose_num(12, 15))  # Should print: 14
print(choose_num(13, 12))  # Should print: -1
print(choose_num(10, 10))  # Should print: 10
print(choose_num(20, 20))  # Should print: 20
print(choose_num(10, 20))  # Should print: 18
print(choose_num(25, 25))  # Should print: 24










```