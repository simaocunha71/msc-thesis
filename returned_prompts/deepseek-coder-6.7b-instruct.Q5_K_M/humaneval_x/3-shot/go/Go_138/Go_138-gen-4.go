    sum := 0
    count := 0
    for i := 2; sum < n || count < 4; i += 2 {
        sum += i
        count += 1
    }
    return sum == n && count == 4
}



