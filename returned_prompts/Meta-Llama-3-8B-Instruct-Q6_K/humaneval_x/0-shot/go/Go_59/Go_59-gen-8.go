    i := 2
    for i * i <= n {
        if n % i == 0 {
            return i
        }
        i += 1
    }
    return n
}

