To convert the number in base to decimal, use the following formula:

sum = 0
while (x > 0):
    sum = sum * base + x % 10
    x = x / 10

Finally, convert the result from decimal to string and return.

Here's a step-by-step guide to solve this problem:

1. Initialize a variable sum to 0. It will be used to store the decimal representation of the number.
2. Use a while loop to iterate until the number becomes 0. Inside the loop, perform the following steps:

    a. Calculate the remainder of x divided by 10. This gives the least significant digit of the number.
    
    b. Update the value of sum by adding the product of the current value of sum and base, and the remainder. This effectively converts the least significant digit from the original base to decimal.
    
    c. Divide x by 10 to remove the least significant digit from the number.
3. After the loop, convert the value of sum from decimal to the desired base. Here's how you can do it:

    a. Initialize an empty string variable result to store the result.
    
    b. Use a while loop to iterate until the value of sum becomes 0. Inside the loop, perform the following steps:

        i. Calculate the remainder of sum divided by base. This gives the least significant digit of the number in decimal.
        
        ii. Convert the remainder to the desired base. For example, if the remainder is 10 and the desired base is 2, the remainder becomes 1010 (binary).
        
        iii. Append the binary representation to the result.
        
        iv. Update the value of sum by dividing it by base. This removes the least significant digit from the number.
    
    c. Return the result.

This algorithm converts a number from one base to another in O(log(x)) time complexity, where x is the number to be converted.

Here's the Python code to implement this algorithm:

def changeBase(x, base):
    # Convert the number from base to decimal
    sum = 0
    while (x > 0):
        sum = sum * base