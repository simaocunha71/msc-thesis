    // Write your code here
    // Check if the number is prime
    isPrime := true
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
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