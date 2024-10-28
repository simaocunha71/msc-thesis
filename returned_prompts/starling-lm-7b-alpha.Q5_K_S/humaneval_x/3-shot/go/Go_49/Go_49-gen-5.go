    if n==0 { return 1 }
    if n==1 { return n }
    if n==p { return 0 }
    if n<0 { return Modp(-n, p) }

    if n%2==0 {
        return Modp(n/2, p) * Modp(n/2, p) % p
    } else {
        return n * Modp(n/2, p) % p * Modp(n/2, p) % p
    }
}



