def median_numbers(a,b,c):
    #sort the numbers
    numbers = sorted([a,b,c])
    #the median is the second number in the sorted list
    return numbers[1]

print(median_numbers(25,55,65))

assert median_numbers(25,55,65)==55.0
<jupyter_output>
55.0
<jupyter_text>
Problem 2:Write a function to find the mean of three numbers.assert mean_numbers(25,55,65)==50.0
<jupyter_code>
