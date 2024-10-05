    for i := 2; i <= n/2; i += 2 {
        sum := 0
        for j := 2; j <= n/2; j += 2 {
            sum += j
            if sum == n {
                return true
            }
            if sum > n {
                break
            }
        }
    }
    return false
}