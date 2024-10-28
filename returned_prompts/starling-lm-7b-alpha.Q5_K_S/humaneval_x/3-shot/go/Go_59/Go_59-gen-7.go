    i := 2
    for i*i <= n {
        if n % i == 0 {
            n /= i
        }else {
            i += 1
        }
    }
    return n
}



