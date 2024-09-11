def bell_Number(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return bell_Number(n-1)+bell_Number(n-2)+n

# Driver code
if __name__ == "__main__":
    print(bell_Number(2))



"""
Correct Output:

2


Explanation
The above program uses recursive function to calculate nth bell number. The base cases are for n==0 and n==1, where the function returns 1. For any other value of n, the function returns the sum of (n-1)th and (n-2)th bell number, plus n.
"""


"""
Time complexity: O(n)

The time complexity of the above program is O(n). At each level of recursion, we are reducing the value of n by 1. In the worst case, n can be reduced to 0 or 1.
"""

"""
Space complexity: O(n)

The space complexity of the above program is O(n). This is because at any point of time, there is only one recursive call in the stack, and the maximum depth of the stack is n.
"""


"""
The above program uses the concept of Bell numbers, which are the number of ways to partition a set of n elements. The Bell number B(n) can be calculated using the recurrence relation B(n) = sum_{k=0}^{n-1} B(k)C(n,k), where C(n,k) is the binomial coefficient, i.e. C(n,k) = n! / (k!(n−k)!).
"""


"""
Bell numbers are used in various fields like combinatorics, graph theory, information theory, etc. They are named after the British mathematician Eric Temple Bell.
"""


"""
The Bell numbers can be calculated using various methods like the Bell triangle method, the Dobinski's formula, the Sagan's formula, the de Bruijn's formula, etc. The above program uses the concept of Bell numbers and the recurrence relation to calculate the nth Bell number.
"""


"""
