def test_three_equal(num1, num2, num3):
    if num1 == num2 == num3:
        return 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return 2
    else:
        return 0

#Test cases
print(test_three_equal(1,1,1)) #3
print(test_three_equal(1,2,1)) #2
print(test_three_equal(1,2,3)) #0
print(test_three_equal(2,2,2)) #3
print(test_three_equal(1,1,2)) #2

"""
Explanation:
In the question, we have to count the number of equal numbers from three given integers.
We can achieve this by using a simple if-elif-else structure. 

If all three numbers are equal, the function will return 3. 
If two numbers are equal, the function will return 2. 
If no numbers are equal, the function will return 0.

We can test the function with various test cases to ensure it's working correctly.
"""
<jupyter_output>
3
2
0
3
2
<jupyter_text>
Q2: Write a Python function to compute the sum of the squares of the first n positive integers.
<jupyter_code>
#Answer:

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

#Test cases
print(sum_of_squares(5)) #55
print(sum_of_squares(6)) #91
<jupyter_output>
55
91
<jupyter_text>
Q3: Write a Python function to compute the sum of the squares of the first n even numbers.
<jupyter_code>
#Answer:

def sum_of_squares_even(n):
    return sum((2*i)**2 for i in range(1, n+1))

#Test cases
print(sum_of_squares_even