func XOrY(n, x, y int) int {
    isPrime := true
    for i := 2; i < n; i++ {
        if n % i == 0 {
            isPrime = false
            break
        }
    }
    if isPrime {
        return x
    } else {
        return y
    }
}