
def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)


print(add([4, 2, 6, 7]))  # 2
print(add([2, 1, 1, 4, 3, 3]))  # 4
print(add([1, 1, 1, 1, 1, 1]))  # 0
print(add([2, 3, 4, 5, 6, 7, 8]))  # 2

# 解答
def add(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 != 0 and x % 2 == 0)

print(add([4, 2, 6, 7]))  # 2
print(add([2, 1, 1, 4, 3, 3]))  # 4
print(add([1, 1, 1, 1, 1, 1]))  # 0
print(add([2, 3, 4, 5, 6, 7, 8]))  # 2
<jupyter_output>
2
4
0
2
<jupyter_text>
Exercise 5: Filtering ListsGiven a list of integers, use list comprehension and the built-in filter function to return a list of integers that are even.
<jupyter_code>
