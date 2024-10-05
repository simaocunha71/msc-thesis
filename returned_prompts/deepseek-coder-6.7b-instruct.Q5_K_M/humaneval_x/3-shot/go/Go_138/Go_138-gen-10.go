    sum := 0
    count := 0
    for i := 2; i <= n; i += 2 {
        sum += i
        count += 1
        if sum == n {
            return true
        }
        if sum > n || count == 4 {
            return false
        }
    }
    return false
}



