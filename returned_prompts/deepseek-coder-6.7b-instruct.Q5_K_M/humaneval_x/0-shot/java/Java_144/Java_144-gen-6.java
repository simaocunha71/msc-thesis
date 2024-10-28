    }
}

'''

'''
def simplify(x: str, n: str) -> bool:
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    return x_num * n_den == x_den * n_num
'''

# Explanation:
# This function takes in two strings x and n which represent fractions. It splits these strings into numerators and denominators, converts them to integers, and then checks if the product of the numerators and denominators of n equals the product of the denominators and numerators of x. If they are equal, it returns True indicating that x * n evaluates to a whole number. If not, it returns False indicating that x * n does not evaluate to a whole number.

# This solution works because the product of the numerators and denominators of a fraction is the same as the product of the denominators and numerators.

# The time complexity is O(1) since the operations are performed in constant time. The space complexity is also O(1) since no additional space is used that scales with the input size.

# This solution is correct because it correctly implements the mathematical definition of simplifying a fraction.
'''



'''
Example 1:
Input: 
x = "1/5"
n = "5/1"
Output: 
True
Explanation: 
1/5 * 5/1 = 1/5 = 0.2, which is a whole number.

Example 2:
Input: 
x = "1/6"
n = "2/1"
Output: 
False
Explanation: 
1/6 * 2/1 = 1/6 = 0.16666666666666666, which is not a whole number.

Example 3:
Input: 
x = "7/10"
n = "10/2"
Output: 
False
Explanation: 
7/10 * 10/2 = 7/10 = 0.7, which is not a whole number.
'''

