    var i int = 2

    for i * i <= n {
        if n % i == 0 {
            n = n / i
        } else {
            i += 1
        }
    }
    return n
}



