
    def is_simple_power(x, n):
        if x==1:
            return True
        elif n==1:
            return False
        else:
            i=2
            while(n**i<=x):
                if n**i==x:
                    return True
                i+=1
            return False

    print(is_simple_power(1, 4)) #=> true
    print(is_simple_power(2, 2)) #=> true
    print(is_simple_power(8, 2)) #=> true
    print(is_simple_power(3, 2)) #=> false
    print(is_simple_power(3, 1)) #=> false
    print(is_simple_power(5, 3)) #=> false

This code defines a function called is_simple_power which takes two parameters: x and n. If x is 1, the function returns True. If n is 1, the function returns False. Otherwise, a while loop is used to check if n raised to an integer i equals x. If it does, the function returns True. If the while loop completes without finding a match, the function returns False. The function is then tested with various inputs.

The function handles edge cases by returning False for x=1 and n=1. The function uses a while loop to check if n raised to an integer i is less than or equal to x. This loop continues until n raised to an integer i is greater than x. The function returns True if n raised to an integer i equals x, and False otherwise.

This function can be used to determine if a number is a simple power of another number.

The time complexity of this function is O(x) as it uses a while loop to check if n raised to an integer i equals x.

The space complexity of this function is O(1) as it uses a constant amount of space to store the variables x, n, and i.

This function can be used in a variety of applications, such as in algorithms for number theory, cryptography, and computer science.

Please note that this function assumes that x and n are non-negative integers. If x or n are negative, the function may not behave as expected.

In conclusion, this function is a useful