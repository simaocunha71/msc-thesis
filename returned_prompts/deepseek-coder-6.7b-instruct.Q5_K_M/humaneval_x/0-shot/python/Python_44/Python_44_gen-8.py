

def change_base(x: int, base: int):
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# 测试函数
print(change_base(8, 3))  # 期望输出: '22'
print(change_base(8, 2))  # 期望输出: '1000'
print(change_base(7, 2))  # 期望输出: '111'
print(change_base(17, 5))  # 期望输出: '20'
print(change_base(1234, 5))  # 期望输出: '142'

# 注意：该函数使用了递归来将数字转换为所需的进制。它通过不断地将数字除以进制，并将余数添加到结果字符串中来实现。这个过程会一直持续到数字小于进制为止。
# 此外，该函数假设输入的数字和进制都是正整数。如果要处理负数和非整数输入，需要进行额外的错误处理。
<jupyter_output>
22
1000
111
20
142
<jupyter_text>
Question 5:Write a Python program that will create a simple calculator. The calculator will take two inputs from the user and perform four basic mathematical operations: addition, subtraction, multiplication, and division. You can use the `input` function to take inputs from the user. For division, you can assume that the user will not input a zero.
<jupyter_code>
# Solution:

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")

    if op == '+':
        print(num1