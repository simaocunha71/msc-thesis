
var primes []int
    for i := 2; i < n; i++ {
        if isPrime(i) {
            primes = append(primes, i)
        }
    }
    return primes
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}


// The function CountUpTo(n) works by iterating over all integers from 2 to n (exclusive),
// checking whether each one is a prime number (using the helper function isPrime()),
// and if so, adding it to the primes slice. The function then returns this slice.

// The function isPrime(n) checks whether a number n is prime by checking whether it
// is divisible by any integer from 2 up to the square root of n (since a larger factor
// of n would be a multiple of a smaller factor that has already been checked). If n
// is less than 2 or if it is divisible by any of these integers, then it is not a prime
// number and the function returns false; otherwise, it is a prime number and the
// function returns true.

// This solution is efficient because the time complexity of the isPrime function is O(sqrt(n)),
// and we call this function n-2 times in the CountUpTo function. Thus, the total time complexity
// of the CountUpTo function is O((n-2) * sqrt(n)), which is approximately O(n sqrt(n)) for large n.
// This is better than the brute force approach of checking all pairs of numbers for primality,
// which would have a time complexity of O(n^2), which is impractical for large n.

// The space complexity of the CountUpTo function is O(n), because in the worst case (when all
// numbers from 2 to n are prime) the primes slice will contain n-2 elements.
// Therefore, the space complexity of this solution is linear.

// Note: The problem statement specifies that the function should return an array of