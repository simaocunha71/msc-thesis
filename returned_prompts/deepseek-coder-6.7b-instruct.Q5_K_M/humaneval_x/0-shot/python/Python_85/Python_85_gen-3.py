
def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2))


print(add([4, 2, 6, 7]))  # 2
print(add([1, 2, 3, 4, 5]))  # 4
print(add([10, 20, 30, 40, 50]))  # 150
print(add([7, 1, 5, 3]))  # 10
print(add([1, 10, 100, 1000, 10000]))  # 10100
<jupyter_output>
2
4
150
10
10100
<jupyter_text>
Problem 3Write a Python program that accepts a string and calculates the number of digits and letters.
<jupyter_code>
