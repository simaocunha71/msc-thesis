    if n == 1 { return 2 }
    if n == 2 { return 3 }
    if n < 0 { return 0 }

    i, fib, prime := 3, 2, 3
    for ; fib < n; i++ {
        fib = fib + prime
        if fib % 2 != 0 && isPrime(fib) {
            return fib
        } else {
            prime = fib + prime
        }
    }
    return 0
}

func isPrime(n int) bool {
    if n <= 1 { return false }
    if n <= 3 { return true }
    if n%2==0 || n%3==0 { return false }
    i := 5
    for ; i * i <= n; i += 6 {
        if n%i==0 || n%(i+2)==0 { return false }
    }
    return true
}



