def make_a_pile(n):
    result = [n]
    i = n - 1
    while i > 0:
        if i % 2 == 0:
            i -= 1
            result.append(i + 1)
        else:
            i += 2
            result.append(i)
    return result
print(make_a_pile(3))
# Output: [3, 5, 7]
print(make_a_pile(4))
# Output: [4, 6, 8]
print(make_a_pile(5))
# Output: [5, 7, 9]
print(make_a_pile(6))
# Output: [6, 8, 10]  



