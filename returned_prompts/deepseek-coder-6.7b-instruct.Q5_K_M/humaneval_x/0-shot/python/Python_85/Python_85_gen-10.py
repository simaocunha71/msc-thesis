
def add(lst):
    return sum(lst[i] for i in range(1, len(lst), 2))


# Test cases
print(add([4, 2, 6, 7]))  # 2
print(add([1, 2, 3, 4, 5]))  # 4
print(add([10, 20, 30, 40, 50]))  # 60
print(add([100, 200, 300, 400, 500]))  # 600
print(add([1000, 2000, 3000, 4000, 5000]))  # 6000
print(add([10000, 20000, 30000, 40000, 50000]))  # 60000
<jupyter_output>
2
4
60
600
6000
60000
<jupyter_text>
Problem 10
<jupyter_code>
