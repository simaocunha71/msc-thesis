
func CountUpTo(n int) []int {
    // check if n is less than 2
    if n < 2 {
        return []int{}
    }

    // initialize an array to store prime numbers
    primes := []int{2}

    // iterate through numbers from 3 to n
    for i := 3; i < n; i++ {
        // check if i is prime
        isPrime := true
        for j := 2; j*j <= i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        // if i is prime, add it to the primes array
        if isPrime {
            primes = append(primes, i)
        }
    }

    return primes
}