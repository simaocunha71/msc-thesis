    i := 2
    for {
        if n%i == 0 {
            n /= i
        } else {
            i += 1
            if i * i > n {
                return n
            }
        }
    }
}