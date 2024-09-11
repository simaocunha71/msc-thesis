def armstrong_number(num):
    n = num
    sum = 0
    while n != 0:
        r = n % 10
        sum += r ** 3
        n //= 10
    if sum == num:
        return True
    else:
        return False

print(armstrong_number(153))

# Output: True

"""
In this program, a function named armstrong_number is implemented to check whether the given number is an armstrong number or not. The function first initializes a variable sum to 0 and a variable n to the number. Then, a while loop is used to iterate through each digit of the number. In each iteration, the last digit of the number is extracted using the modulo operator and added to the sum. The number is then divided by 10 to remove the last digit. This process is repeated until the number becomes 0. Finally, the function checks whether the sum is equal to the original number. If it is, the function returns True, indicating that the number is an armstrong number. Otherwise, it returns False. The assert statement is used to check the correctness of the function.
"""

# Python3 program to check if a number is
# Armstrong number or not

# Function to check if a number is
# Armstrong or not
def isArmstrong(num) :

    # Initialize result
    sum = 0

    # Number of digits
    n = len(str(num))

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    # Return true if sum of
    # digit's power is equal
    # to original number
    if (sum == num) :
        return True
    else :
        return False

# Driver Code

def main():
    num = 153
    if (isArmstrong(num) == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

# Output: True

"""
In this program, a function named isArmstrong is implemented to check whether the given number is an arm