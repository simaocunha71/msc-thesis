
def f(n):
    def factorial(x):
        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def summation(x):
        return x * (x + 1) // 2

    return [factorial(i) if i % 2 == 0 else summation(i) for i in range(1, n + 1)]

print(f(5))

# Test cases
assert f(5) == [1, 2, 6, 24, 15]
assert f(1) == [1]
assert f(0) == []
assert f(6) == [1, 2, 6, 24, 15, 132]
assert f(10) == [1, 2, 6, 24, 15, 132, 252, 1624, 720, 2015]
assert f(20) == [1, 2, 6, 24, 15, 132, 252, 1624, 720, 2015, 26572, 54744, 85800, 113379, 130873, 133216, 125463, 105511, 79070]

# In the end, call the function with the number of test cases you want to test.
f(20)
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 5
<jupyter_code>
