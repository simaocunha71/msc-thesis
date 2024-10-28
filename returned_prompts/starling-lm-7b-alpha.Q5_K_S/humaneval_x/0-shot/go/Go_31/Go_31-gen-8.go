
func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 || n == 3 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    if n%3 == 0 {
        return false
    }

    i := 5
    for i * i <= n {
        if n%i == 0 {
            return false
        }
        if n%(i+2) == 0 {
            return false
        }
        i += 6
    }

    return true
}


Explanation:

To check if a number is prime, you only need to check up to the square root of that number, as factors larger than the square root would have corresponding factors smaller than the square root.

In this implementation, if the number is less than or equal to 1, it is not prime. If the number is 2 or 3, it is prime. If the number is divisible by 2, it is not prime. If the number is divisible by 3, it is not prime.

After these initial checks, we start a loop from 5 and increment by 6 in each iteration. This is because all prime numbers greater than 3 can be expressed in the form 6k ± 1, and skipping the multiples of 2 and 3 helps in reducing the number of iterations.

Inside the loop, we check if the number is divisible by the current value of i or i+2. If it is, the number is not prime and we return false. If the loop completes without finding any factors, the number is prime and we return true.

This implementation efficiently checks if a number is prime or not.










































































































