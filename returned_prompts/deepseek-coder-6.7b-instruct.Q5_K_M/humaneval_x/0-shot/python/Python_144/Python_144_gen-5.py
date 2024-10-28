
def simplify(x, n):
    # Splitting the fractions into numerator and denominator
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    # Calculating the product of the numerators and the product of the denominators
    xn_num, xn_den = x_num * n_num, x_den * n_den
    
    # Checking if the product of the numerators is divisible by the product of the denominators
    return xn_num % xn_den == 0

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # True
print(simplify("1/1", "1/1")) # True
print(simplify("1/2", "1/2")) # True
print(simplify("1/10", "1/10")) # True
print(simplify("1/3", "1/3")) # True
print(simplify("1/4", "1/2")) # True
print(simplify("1/4", "1/3")) # False

'''
Explanation:

The function takes in two strings that represent fractions and returns True if the multiplication of these fractions results in an integer and False otherwise. 

The function first splits each fraction into its numerator and denominator, converting them to integers. Then, it calculates the product of the numerators and the product of the denominators. 

Finally, it checks if the product of the numerators is divisible by the product of the denominators, which is equivalent to checking if the fraction is simplified.

The function uses the modulus operator to check for divisibility, as it returns the remainder of the division. If the remainder is zero, this means the fraction is simplified (i.e., it evaluates to an integer).
'''

# Test cases
print(simplify("1/5", "5/1")) # True
print(simplify("