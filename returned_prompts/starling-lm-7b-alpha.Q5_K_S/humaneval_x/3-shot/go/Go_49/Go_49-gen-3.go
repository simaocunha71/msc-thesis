    if n < 0 {
        return Modp(-n,p)
    }
    result := 1
    while n > 0 {
        if n % 2 == 1 {
            result = result * p % p
        }
        n /= 2
        p = p * p % p
    }
    return result
}



