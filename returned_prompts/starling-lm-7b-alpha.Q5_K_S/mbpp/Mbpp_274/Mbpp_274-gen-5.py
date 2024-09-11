def even_binomial_Coeff_Sum(n):
    assert(n>=1)
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += 1
    return sum

def test_even_binomial_Coeff_Sum():
    assert(even_binomial_Coeff_Sum(4) == 8)

test_even_binomial_Coeff_Sum()


"""
Explanation:
The binomial coefficient, denoted as C(n, k), is the number of ways to choose k items from a set of n items without regard to the order of selection. It is usually denoted as nCk or "n choose k". It is also called a binomial coefficient because it appears as the coefficients of the binomial theorem.

The sum of the even indexed values of a binomial coefficient sequence is equal to 2^n. This can be proven by induction, since the binomial coefficient is symmetric around the middle.

In the given function, we first check if the input n is a positive integer. If not, we raise an assertion error. Then, we initialize a variable sum to 0. We then use a for loop to iterate through all the binomial coefficients from 0 to n. Inside the loop, we check if the index is even. If it is, we add 1 to the sum. Finally, we return the sum.

In the test function, we check if the function returns the correct result for the given input 4. We assert that the result is equal to 8, and if it is not, the test will fail.
"""

# Python3 program to find
# all prime factors of a number

# Function to find all prime factors
# of a number n
def primeFactors(n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        print (2, end = " ");
        n = n / 2
          
    # n must be odd at this point.  So we can
    # skip one element (Note i = i +2)
    for i in range(3,int(n**0.5