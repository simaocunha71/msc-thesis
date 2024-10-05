    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if is_prime(n):
        return x
    else:
        return y

# Testing the function
print(x_or_y(7, 34, 12))  # Expected output: 34
print(x_or_y(15, 8, 5))   # Expected output: 5
print(x_or_y(2, 10, 20))  # Expected output: 20
print(x_or_y(3, 100, 50)) # Expected output: 100
print(x_or_y(10, 10, 20)) # Expected output: 20
print(x_or_y(11, 30, 40)) # Expected output: 30

# Example usage with a function that checks if a number is prime
def check_prime(n):
    if is_prime(n):
        return "Prime"
    else:
        return "Not Prime"

for i in range(1, 20):
    print(f"{i} is {check_prime(i)}")  # Checking if each number is prime or not
    if is_prime(i):
        print(f"The number {i} is a prime number")
    else:
        print(f"The number {i} is not a prime number")  # Testing the function
print(f"Is 17 a prime number? {is_prime(17)}")  # Testing the function
print(f"Is 18 a prime number? {is_prime(18)}")  # Testing the function
print(f"Is 2 a prime number? {is_prime(2)}")  # Testing the function
print(f"Is 3 a prime number? {is_prime(3)}")  # Testing the function
print(f"Is 4 a prime number? {is_prime(4)}")  # Testing the function
print(f"Is 5 a prime number? {is_prime(5)}")  # Testing the function
print(f"Is 6 a prime number? {is_prime(6)}")  # Testing the function
print(f"Is 7 a prime number? {is_prime(7)}")  # Testing the function
print(f"Is 8 a prime number? {is_prime(8