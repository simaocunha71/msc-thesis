def fib_sum(limit):
    sum, a, b = 0, 1, 2
    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum

print(fib_sum(10))
print(fib_sum(100))
print(fib_sum(4000000))
<jupyter_output>
10
44
4613732
<jupyter_text>
Problem 6: Multiples of 3 and 5If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.assert