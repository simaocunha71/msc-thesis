func IsMultiplyPrime(a int) bool {
    primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    for _, p := range primes {
        if a % p == 0 {
            a /= p
            if a == 1 {
                return true
            }
        }
    }
    return false
}