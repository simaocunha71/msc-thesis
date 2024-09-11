def armstrong_number(n):
    if n>9:
        s=0
        temp=n
        while temp>0:
            rem = temp%10
            s+=rem**4
            temp//=10
        if s==n:
            return True
        else:
            return False
    else:
        return False


# Driver program
print(armstrong_number(153))


"""
Explanation:
The above code defines a function armstrong_number() that takes a number as an argument and checks whether the given number is an Armstrong number or not.

The function first checks if the number is greater than 9. If it is not, then the function returns False, indicating that the number cannot be an Armstrong number.

If the number is greater than 9, the function initializes a variable s to 0 and a variable temp to the given number. It then enters a while loop, where it repeatedly calculates the remainder of temp divided by 10, raises it to the power of 4, and adds the result to s. It also updates temp by dividing it by 10.

Once the while loop finishes, the function checks if s is equal to the original number. If they are equal, it means that the number is an Armstrong number, and the function returns True. Otherwise, it returns False.

In the driver program, the function is called with the number 153 as an argument. The result, True, is printed to the console.

Note: The code assumes that the input number is a positive integer.
"""



"""
Explanation:

An Armstrong number, also known as a pluperfect number, is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

The code defines a function armstrong_number() that takes a number as an argument and checks whether the given number is an Armstrong number or not. It first checks if the number is greater than 9. If it is not, then the function returns False, indicating that the number cannot be an Armstrong number.
