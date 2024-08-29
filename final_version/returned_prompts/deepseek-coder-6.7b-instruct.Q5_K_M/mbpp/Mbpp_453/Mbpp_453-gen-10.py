def sumofFactors(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and i % 2 == 0:
            sum += i
    return sum

print(sumofFactors(18))

# Output: 26

Explanation:
The function sumofFactors takes an integer as input and returns the sum of all even factors of that number. The factors are the numbers that evenly divide the number. The loop iterates over each number from 1 to the input number (inclusive), checks if the number is a factor (i.e. if the remainder of the division is 0), and if it is, checks if it is an even number (i.e. if it is divisible by 2). If both conditions are met, the factor is added to the sum. The function then returns the sum.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
