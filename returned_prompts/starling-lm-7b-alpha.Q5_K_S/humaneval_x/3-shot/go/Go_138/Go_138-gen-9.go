    for i := 2; i <= n / 2; i += 2 {
        if n - i == 2 * (i + 1) {
            return true
        }
    }
    return false
}



