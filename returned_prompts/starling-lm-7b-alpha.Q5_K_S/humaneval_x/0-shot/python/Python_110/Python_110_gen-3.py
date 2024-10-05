
def exchange(lst1, lst2):
    lst1_odd = []
    for i in lst1:
        if i % 2 != 0:
            lst1_odd.append(i)
    if len(lst1_odd) == 0:
        return "YES"
    for i in lst2:
        if i % 2 != 0:
            if len(lst1_odd) == 0:
                return "NO"
            else:
                lst1.remove(lst1_odd.pop())
    return "YES"


# 测试
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # 应该输出: "YES"
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # 应该输出: "YES"
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # 应该输出: "NO"

# 更多测试
print(exchange([1, 2, 3, 4], [3, 4, 5, 6]))  # 应该输出: "YES"
print(exchange([1, 2, 3, 4], [7, 8, 9, 10]))  # 应该输出: "NO"
print(exchange([1, 2, 3, 4], [7, 8, 9, 11]))  # 应该输出: "NO"
print(exchange([1, 2, 3, 4], [7, 8, 9, 10, 11]))  # 应该输出: "NO"
print(exchange([1, 2, 3, 4], [7, 8, 9, 10, 11, 12]))  # 应该输出: "YES"
print(exchange([1, 3, 5, 7