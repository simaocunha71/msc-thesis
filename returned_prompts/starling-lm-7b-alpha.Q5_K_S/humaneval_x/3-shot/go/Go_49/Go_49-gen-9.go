    if n < 0 {
        return Modp(-n, p)
    }
    if p == 1 {
        return 0
    }
    if p == 0 {
        return 1
    }
    if n == 0 {
        return 1
    }
    if n < p {
        return n
    }
    if n < p / 2 {
        return n
    }
    return n % p + Modp(n / p, p)
}





