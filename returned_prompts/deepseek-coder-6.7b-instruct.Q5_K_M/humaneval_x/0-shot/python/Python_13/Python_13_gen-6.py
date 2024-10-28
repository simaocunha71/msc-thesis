
    if a == 0 and b != 0:
        return b
    elif b == 0 and a != 0:
        return a
    else:
        while b != 0:
            a, b = b, a % b
        return a


print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))
print(greatest_common_divisor(0, 5))
print(greatest_common_divisor(5, 0))
print(greatest_common_divisor(0, 0))

# 1
# 5
# 5
# 0
# 0
# 说明：
# 第一个测试用例中，3和5的最大公约数是1。
# 第二个测试用例中，25和15的最大公约数是5。
# 第三个和第四个测试用例中，当其中一个数为0时，最大公约数为非0数。如果两个数都为0，则最大公约数未定义，返回0。
<jupyter_output>
1
5
5
0
0
<jupyter_text>
问题3. 编写一个Python函数，它以一个整数作为输入，并返回该整数的阶乘。
<jupyter_code>
