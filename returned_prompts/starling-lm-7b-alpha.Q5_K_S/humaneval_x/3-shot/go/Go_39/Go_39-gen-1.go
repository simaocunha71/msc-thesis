    if n == 1 {
        return 2
    }
    if n == 2 {
        return 3
    }
    a, b := 2, 3
    for i := 3; i <= n; i++ {
        a, b = b, a+b
        if i == n {
            return a
        }else if a+b > 1e6 {
            continue
        }
        if a > 1e6 {
            continue
        }
        if !Prime(a) {
            continue
        }
        if a+b > 1e6 {
            continue
        }
        if !Prime(b) {
            continue
        }
        if a+b > 1e6 {
            continue
        }
        if Prime(a+b) {
            continue
        }
    }
    return -1
}



