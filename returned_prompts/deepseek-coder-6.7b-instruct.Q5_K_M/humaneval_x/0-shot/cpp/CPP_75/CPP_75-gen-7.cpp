This is a C++ solution.
The function is_multiply_prime first checks if the input number is a prime number. If it is, it returns false because a number can't be a multiplication of 3 prime numbers if it's a prime number. If the input number is not a prime number, it counts the factors of the number. If the count is 3, it means the number is the multiplication of 3 prime numbers. If the count is not 3, it means the number is not the multiplication of 3 prime numbers.

This solution uses the Sieve of Eratosthenes algorithm to generate all prime numbers up to 100. The Sieve of Eratosthenes is a very efficient way to find all primes smaller than n when n is smaller than 10 million.

In the main function, the user is asked to enter a number. The function is_multiply_prime is called with the entered number as the argument. The result is then printed to the console.

The time complexity of this solution is O(n log log n) for the Sieve of Eratosthenes and O(n) for the is_multiply_prime function. This means that the overall time complexity of the solution is O(n log log n), which is efficient for large inputs.

The space complexity of this solution is O(n) for the Sieve of Eratosthenes and O(1) for the is_multiply_prime function. This means that the overall space complexity of the solution is O(n),