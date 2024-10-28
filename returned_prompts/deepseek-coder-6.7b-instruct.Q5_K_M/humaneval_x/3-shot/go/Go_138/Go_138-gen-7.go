    sum := 0
    count := 0
    i := 2

    for sum < n {
        sum += i
        count++
        i += 2

        if sum == n && count == 4 {
            return true
        }
    }

    return false
}

