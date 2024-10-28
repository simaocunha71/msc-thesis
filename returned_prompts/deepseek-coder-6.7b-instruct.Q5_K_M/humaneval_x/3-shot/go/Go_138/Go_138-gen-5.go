    count := 0
    sum := 0
    for i := 2; i <= n; i += 2 {
        if count == 4 {
            break
        }
        sum += i
        count++
    }
    return sum == n
}



