
def find_Odd_Pair(arr, n): 
    odd_count = 0
    for i in range(0, n): 
        if ((arr[i] ^ 1) in arr): 
            odd_count += 1
    return odd_count 

print(find_Odd_Pair([5,4,7,2,1],5)) # 6

Explanation:
The XOR operator "^" returns a number that is the result of performing the binary XOR operation on the two numbers. XOR is a binary operator that takes two equal-length binary representations, and performs the logical XOR operation on each pair of corresponding bits.
Here, the XOR of a number with 1 always gives the number with its least significant bit flipped.
If the number is even, then XOR of that number with 1 will make it odd. Conversely, if the number is odd, then XOR of that number with 1 will make it even.
Thus, the function first checks if the XOR of a number with 1 is present in the array or not. If it is present, then it means that the pair of the number and its XOR with 1 is an odd pair, and it increments the counter. Finally, it returns the count of such pairs.

"""

