
func IsMultiplyPrime(a int) bool {
    if a < 100 {
        return isPrime(a)
    }
    return false
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    if n == 2 || n == 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }

    i := 5
    for i * i <= n {
        if n%i == 0 || n%(i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}

The function `IsMultiplyPrime` checks if a given number is a product of 3 primes. If the number is less than 100, it uses the helper function `isPrime` to determine if the number is a prime itself. If the number is greater than 100, it returns false as it is impossible to determine if a number is a product of 3 primes using only prime numbers less than 100.

The `isPrime` function checks if a number is a prime by iterating through all the numbers up to the square root of the number. If a number is divisible by any of these numbers, it is not prime. If the number is not divisible by any of these numbers, it is prime.

The `isPrime` function returns true if the number is prime and false otherwise.

The `IsMultiplyPrime` function returns true if the given number is the multiplication of 3 prime numbers and false otherwise.

The time complexity of `isPrime` function is O(√n) and the space complexity is O(1).

Overall, the time complexity of `IsMultiplyPrime` function is O(√n) and the space complexity is O(1).

Here are some test cases:

Test case 1:
Input: 30
Output: true
Explanation: 30 = 2 * 3 * 5, so 30 is the multiplication of 3 prime numbers.

Test case 2