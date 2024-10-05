

def add(x: int, y: int):
    return x + y
```

## 1.3 多行文档字符串

如果你的函数或类有多个文档字符串行，你可以在末尾添加一个三引号 `"""` 来标记文档字符串的结束。例如：

```python
def function_name(arguments):
    """
    这里是第一行文档字符串。
    这里是第二行文档字符串。
    ...
    """
```

## 1.4 多行注释

在Python中，多行注释使用 `''' '''` 或者 `""" """"` 来包裹。

```python
'''
这是一个多行注释
这是第二行
这是第三行
'''
```

或者

```python
"""
这是一个多行注释
这是第二行
这是第三行
"""
```

# 2. 变量

在Python中，变量名由字母、数字和下划线组成，但不能以数字开头。Python对大小写敏感，因此 `myVariable` 和 `myvariable` 是两个不同的变量。

## 2.1 变量赋值

在Python中，你可以使用 `=` 运算符来赋值。例如：

```python
x = 5
y = "Hello, World!"
```

## 2.2 多个变量赋值

在Python中，你可以同时为多个变量赋值。例如：

```python
x, y, z = "Orange", "Banana", "Cherry"
```

## 2.3 变量类型

Python是一种动态类型语言，这意味着你不需要在定义变量时指定变量的类型。Python会根据你给变量赋的值来推断出变量的类型。例如：

```python
x = 5
print(type(x))  # <class 'int'>

x = "Hello, World!"
print(type(x))  # <class 'str'>
```

# 3. 数据类型
