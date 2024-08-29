
def find_Odd_Pair(arr, n):
    odd = 0
    even = 0
    for i in range(0, n):
        if (arr[i] & 1):
            odd += 1
        else:
            even += 1
    return odd * even

print(find_Odd_Pair([5,4,7,2,1],5))


# The logic behind the solution is that if there are odd number of odd numbers and even numbers in the array, 
# then the XOR operation will result in an odd number. Thus, we are counting the number of odd numbers and even numbers 
# in the array separately and then multiplying the counts to get the total number of pairs that will result in an odd XOR value.

# The bitwise AND operation (&) is used to determine if a number is odd or even. If the result of arr[i] & 1 is 1, 
# then the number is odd and if the result is 0, then the number is even.

# The time complexity of this solution is O(n), where n is the size of the array. This is because we are performing a 
# single pass through the array to count the number of odd and even numbers.

# The space complexity of this solution is O(1), as we are using a constant amount of space to store the counts of odd 
# and even numbers.

# This solution assumes that the input array only contains positive integers. If the array can contain negative numbers, 
# then the bitwise AND operation should be changed to (arr[i] % 2) to correctly determine if a number is odd or even.

# This solution works because the XOR operation returns 1 if the two bits are different and 0 if they are the same. 
# In binary representation, odd numbers always have their least significant bit set to 1 and even numbers always have 
# their least significant bit set to 0. So, the XOR operation will always result in an odd number if one of the numbers 
# is odd and the other is even.

# This solution is a simple and efficient way to solve the problem.
<jupyter_output>
6
<jupyter_text>
