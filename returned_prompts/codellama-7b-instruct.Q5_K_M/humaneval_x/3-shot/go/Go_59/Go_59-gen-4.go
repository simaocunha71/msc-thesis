    for i := n - 1; i > 1; i-- {
        if n % i == 0 && IsPrime(i) {
            return i
        }
    }
    return 1
}



