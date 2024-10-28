    var i int = 2
    for i * i <= n {
        if n % i != 0 {
            i += 1
        } else {
            n /= i
        }
    }
    return n
}



