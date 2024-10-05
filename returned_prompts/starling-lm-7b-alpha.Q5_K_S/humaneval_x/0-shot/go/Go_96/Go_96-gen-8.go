
func CountUpTo(n int) []int {
    if n < 2 {
        return []int{}
    }

    primes := []int{2}
    for i := 3; i < n; i += 2 {
        isPrime := true
        for j := 2; j*j <= i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            primes = append(primes, i)
        }
    }

    return primes
}


Explanation:
In this problem we need to find all the prime numbers till n and return them in the form of an array.

First we check if the given number is less than 2, in which case we return an empty array, as there are no prime numbers less than 2.

We start our loop from 3, as 2 is the only prime number till then. We increment i by 2 in each iteration, as all even numbers greater than 2 are not prime.

Inside the loop, we check if the current number i is a prime number or not. We do this by iterating from 2 to sqrt(i) and checking if i is divisible by any of these numbers. If it is divisible, we mark it as not prime and break the inner loop. If it is not divisible, we mark it as prime and add it to the result array.

Finally, we return the result array.


































































































































































