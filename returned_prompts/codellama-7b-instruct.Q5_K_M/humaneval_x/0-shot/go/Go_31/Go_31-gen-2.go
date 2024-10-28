
// Return true if a given number is prime, and false otherwise.
// >>> IsPrime(6)
// false
// >>> IsPrime(101)
// true
// >>> IsPrime(11)
// true
// >>> IsPrime(13441)
// true
// >>> IsPrime(61)
// true
// >>> IsPrime(4)
// false
// >>> IsPrime(1)
// false
func IsPrime(n int) bool {

    if n < 2 {
        return false
    }

    // 2 is the only even number that is prime.
    if n == 2 {
        return true
    }

    // If the number is odd, it is prime only if it is greater than 1.
    if n%2 == 0 {
        return false
    }

    // for (i = 3; i <= sqrt(n); i += 2)
    for i := 3; i*i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }

    return true
}
