
// Return the largest prime factor of n. Assume n > 1 and is not a prime.
// >>> LargestPrimeFactor(13195)
// 29
// >>> LargestPrimeFactor(2048)
// 2
func LargestPrimeFactor(n int) int {
    if n == 1 {
        return 1
    }

    // We can start by dividing by 2 because 2 is the smallest prime factor.
    for n%2 == 0 {
        n /= 2
    }

    // Now n is either odd or a prime number.
    if n%2 == 0 {
        return n
    }

    // Now n is an odd number. We can start by dividing by 3 because 3 is the smallest odd prime.
    for n%3 == 0 {
        n /= 3
    }

    // Now n is either a prime number or not divisible by 3.
    if n%3 == 0 {
        return n
    }

    // We can now find the largest prime factor of n by repeatedly dividing n by the smallest prime factor that is greater than 1 and n is not divisible by it.
    // We will keep dividing until n is 1.
    for {
        for i := 5; i*i <= n; i += 6 {
            if n%i == 0 {
                n /= i
                continue A
            }
            if n%(i+2) == 0 {
                n /= i + 2
                continue A
            }
        }
        return n
    }
}
