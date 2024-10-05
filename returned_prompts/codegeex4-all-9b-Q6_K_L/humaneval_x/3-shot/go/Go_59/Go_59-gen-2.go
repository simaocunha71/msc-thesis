    i := 2
    for n > 1 {
        if n%i == 0 {
            n = n / i
        } else {
            i++
        }
    }
    return i
}



