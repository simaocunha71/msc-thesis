

    return sorted(set(l1) & set(l2))

print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))


# 使用集合操作可以使代码更清晰、更高效。
# 在集合操作中，交集（&）用于找到两个集合中的共同元素。
# 然后使用内置的sorted函数对结果列表进行排序。

# 当运行此代码时，它会显示：
# [1, 5, 653]
# [2, 3]
# 这是预期的结果。
<jupyter_output>
[1, 5, 653]
[2, 3]
<jupyter_text>
Problem 5:
<jupyter_code>
