    if n >= p {
        return Modp(n%p,p)
    }else if n < 0 {
        return Modp(n+p,p)
    }else {
        return n
    }
}



