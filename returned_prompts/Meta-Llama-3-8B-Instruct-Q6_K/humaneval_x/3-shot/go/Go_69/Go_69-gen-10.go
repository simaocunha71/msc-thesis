    max := 0
    count := 0
    for _, num := range lst {
        if num > max {
            max = num
            count = 1
        } else if num == max {
            count++
        }
    }
    if count < max {
        return -1
    }
    return max
}