def Find_Max_Length(input_list):
    max_length = 0
    for sublist in input_list:
        if len(sublist) > max_length:
            max_length = len(sublist)
    return max_length

# 测试
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
print("测试通过！")


"""
Explanation:
This function uses a for loop to iterate through each sublist in the input list. It compares the length of each sublist with the current maximum length and updates the maximum length if a longer sublist is found. Finally, it returns the maximum length.
"""

"""
Python提供了内置函数len()来获取列表的长度。这个函数接受一个序列作为参数并返回其长度。
"""

"""
在Python中，列表是一种有序的集合，可以包含多种类型的数据。列表使用方括号表示，列表中的元素用逗号隔开。
"""

"""
在Python中，函数是一种可以执行某个任务或计算的代码块。函数可以接受输入（称为参数），执行某些操作，并返回一个或多个输出（称为返回值）。函数可以简化代码，使其更易于维护和重用。
"""

"""
在Python中，assert关键字用于检查一个条件是否满足。如果条件为真，则不执行任何操作。如果条件为假，则引发一个AssertionError异常。这在调试阶段非常有用，可以帮助发现错误。
"""

"""
在Python中，"=="符号表示相等于。它用于比较两个值是否相等。如果两个值相等，则返回True，否则返回False。
"""

"""
在Python中，"assert"关键字用于检