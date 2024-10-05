
def f(n):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    def sum_of_numbers(num):
        return num * (num + 1) // 2

    return [factorial(i) if i % 2 == 0 else sum_of_numbers(i) for i in range(1, n+1)]

print(f(5))
<jupyter_output>
[1, 2, 6, 24, 15]
<jupyter_text>
Question 2:
<jupyter_code>
