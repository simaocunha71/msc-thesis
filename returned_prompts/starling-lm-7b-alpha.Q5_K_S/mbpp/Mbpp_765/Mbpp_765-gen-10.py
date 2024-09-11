"""
A polite number is a positive integer in which no digit appears more than once, and all the digits are in ascending order. For example, 12345 is a polite number. The function is_polite should take an integer as input and return True if the integer is a polite number and False otherwise. For example, is_polite(12345) should return True, but is_polite(34521) should return False.

Here is a step-by-step guide to finding the nth polite number:

1. Create a function, polite_number, that takes a single argument, n, where n is the position of the desired polite number in the sequence (i.e., the nth polite number). The function will generate the desired polite number and return it.

2. Inside the function, create a variable, used, to store the digits that have already been used in the current polite number. Initialize the variable to an empty string.

3. Create a variable, result, to store the current polite number being generated. Initialize the variable to an empty string.

4. Use a while loop to generate the polite number. In the loop, use a for loop to iterate over the range of all available digits (0 to 9). Check if the current digit is not present in the used digits. If the current digit is not present in the used digits, add the current digit to the result and remove it from the used digits. If the current digit is present in the used digits, continue to the next iteration of the for loop.

5. Once the while loop is complete, return the result. This will be the nth polite number.

6. Write a test function, test_polite_number, to test the polite_number function. The function should call the polite_number function with a variety of inputs and compare the result with the expected output. If the result is as expected, print a message indicating that the test passed; otherwise, print a message indicating that the test failed.
"""
def is_polite(num):
    digits = set(str(num))
    return len(digits) == 1 and sorted(digits) == digits

def polite_number(n):
    used = ""
    result = ""

    while True: