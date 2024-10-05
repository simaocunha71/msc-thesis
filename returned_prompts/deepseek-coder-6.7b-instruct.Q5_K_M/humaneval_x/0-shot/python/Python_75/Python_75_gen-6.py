
    def is_prime(n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        """Checks if a number is the multiplication of 3 prime numbers."""
        factors = []
        for i in range(2, a + 1):
            if a % i == 0 and is_prime(i):
                factors.append(i)
        if len(factors) == 3 and a == factors[0] * factors[1] * factors[2]:
            return True
        else:
            return False

print(is_multiply_prime(30))  # True

# Python program to check if a number is a multiply of 3 prime numbers and false otherwise.
# It uses the is_prime function to check if a number is prime. Then it checks if the number is 
# the multiplication of 3 prime numbers by iterating over all numbers up to the given number and 
# checking if they are prime and if the given number is divisible by them. If these conditions 
# are met, then the number is the multiplication of 3 prime numbers.
# The time complexity of this program is O(n) because in the worst case it checks all numbers up to n.
# The space complexity is O(1) because it uses a constant amount of space to store the factors.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:
<jupyter_code>
