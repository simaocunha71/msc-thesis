def amicable_numbers_sum(n):
    def sum_proper_divisors(x):
        sum = 1
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if i == x / i:
                    sum += i
                else:
                    sum += i + x / i
        return sum

    result = 0
    for i in range(1, n + 1):
        if i == sum_proper_divisors(sum_proper_divisors(i)) and i != sum_proper_divisors(i):
            result += i
    return result

print(amicable_numbers_sum(999))
assert amicable_numbers_sum(999)==504
<jupyter_output>
504
<jupyter_text>
Problem 3Write a function that, given an integer, will return the number of steps it takes for a number to reach 1 following the rules below:If the number is even, divide it by 2.If the number is odd, multiply it by 3 and add 1.The function should return the number of steps taken to reach 1.For example, given the number 7, the steps would be as follows:7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1Steps taken: 16
<jupyter_code>
