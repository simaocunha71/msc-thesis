/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
B:
/*
Return n-th Fibonacci number.
>>> fib(10)
55
>>> fib(1)
1
>>> fib(8)
21
*/
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

A和B哪个更好？

A和B的代码基本相同，都是计算第n个斐波那契数。在Python中，这种递归方法虽然简单，但在处理较大的n时效率会非常低，因为它会进行大量的重复计算。

在A中，代码的缩进似乎有误，`using namespace std;` 这一行应该移到函数定义之外。

在B中，代码的缩进是正确的，并且添加了函数注释，这有助于理解代码的功能。

因此，如果考虑可读性和正确性，B是更好的选择。但如果你需要优化性能，可能需要使用其他方法，如动态规划或矩阵快速幂。