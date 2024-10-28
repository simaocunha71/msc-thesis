    if n > p {
        n = n % p
    }
    if n < 0 {
        n = n % p + p
    }
    return n
}



