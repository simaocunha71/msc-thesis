    sum := 0
    for i := 2; i <= n; i += 2 {
        sum += i
        if sum == n {
            return true
        }
    }
    return false
}


