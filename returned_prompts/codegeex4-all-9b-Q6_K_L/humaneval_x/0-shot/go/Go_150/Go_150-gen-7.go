func XOrY(n, x, y int) int {
    // check if n is prime
    for i := 2; i < n; i++ {
        if n % i == 0 {
            return y
        }
    }
    return x
}