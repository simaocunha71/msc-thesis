
def median_numbers(num1, num2, num3):
    sorted_numbers = sorted([num1, num2, num3])
    return sorted_numbers[1]

print(median_numbers(25,55,65))

# Expected output: 55.0

# Note: In this solution, we first sort the numbers, and then return the middle number, which is the median.
# This works because the median is the middle number in a sorted list of numbers.
<jupyter_output>
55.0
<jupyter_text>
Solution 2:Using Arithmetic Operations
<jupyter_code>
def median_numbers(num1, num2, num3):
    max_num = max(num1, num2, num3)
    min_num = min(num1, num2, num3)
    return num1 + num2 + num3 - max_num - min_num

print(median_numbers(25,55,65))

# Expected output: 55.0

# Note: In this solution, we first find the maximum and minimum numbers, and then return the sum of all three numbers minus the maximum and the minimum, which is the median.
# This works because the median is the middle number in a sorted list of numbers.
<jupyter_output>
55.0
<jupyter_text>
Solution 3:Using Statistics Module
<jupyter_code>
import statistics

def median_numbers(num1, num2, num3):
    return statistics.median([num1, num2, num3])

print(median_numbers(25,55,65))

# Expected output: 55.0

# Note: In this solution, we use the median function from the statistics module to find the median.
<jupyter_output>
55.0
<jupyter_text>
Testing the Functions
<jupyter_code>
assert median_numbers(25,55,65)==55.0