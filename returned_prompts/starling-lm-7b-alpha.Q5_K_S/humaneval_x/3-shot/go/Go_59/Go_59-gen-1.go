    var i = 2
    for i <= n {
        if n % i != 0 {
            i += 1
            continue
        }
        for i < n / i {
            if n % i == 0 {
                return i
            }
            i += 1
        }
        return n / i
    }
    return 1
}



