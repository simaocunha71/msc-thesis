def is_Sum_Of_Powers_Of_Two(n):
    # Initially, we will assume that the given number is not a sum of non-zero powers of 2
    isSum = False

    # We will start from the largest power of 2 that is <= n
    power = 1 << 30

    # We will keep decreasing the power while n is still greater than 0
    while power > 0:
        # If n is greater than or equal to the current power, then we will check if n is equal to 2^power + 2^(power - 1) + ... + 2^(power - power + 1)
        if n >= power:
            temp = power
            while temp > 0:
                if n < (power + temp):
                    break
                temp = temp - 1
            else:
                # If n is equal to 2^power + 2^(power - 1) + ... + 2^(power - power + 1), then we will set isSum to True and break the loop
                isSum = True
                break
        # We will decrease the power by half
        power = power >> 1

    # We will return the value of isSum
    return isSum

"""
Test case 1:
Input:
n = 10
Output:
True
Expected Output:
True

Test case 2:
Input:
n = 3
Output:
False
Expected Output:
False

Test case 3:
Input:
n = 7
Output:
False
Expected Output:
False

Test case 4:
Input:
n = 15
Output:
True
Expected Output:
True

Test case 5:
Input:
n = 31
Output:
True
Expected Output:
True
"""