

def fib(n: int):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))
print(fib(1))
print(fib(8))


# 这个函数使用递归来计算Fibonacci序列。然而，由于递归调用中存在重复计算，所以该函数的时间复杂度是指数级的。
# 可以通过使用动态规划来优化它，以存储和重用先前计算的Fibonacci数。

# 优化后的函数

def fib(n: int):
    fib_values = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    return fib_values[n]


print(fib(10))
print(fib(1))
print(fib(8))


# 这个优化后的函数使用迭代的方法，避免了递归的开销，并且不需要重复计算，因此时间复杂度是线性的。
<jupyter_output>
55
1
21
<jupyter_text>
编程题 2： 在Python中实现一个快速排序算法。快速排序是一种分治算法，它通过选择一个“枢轴”元素，将输入数组分为两个子数组，一个子数组包含小于枢轴的元素，另一个子数组包含大于枢轴的元素，然后对子数组递归地应用这个过程。
<jupyter_code>
