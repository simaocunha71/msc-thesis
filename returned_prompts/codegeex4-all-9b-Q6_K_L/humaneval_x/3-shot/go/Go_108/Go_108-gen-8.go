    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        for num > 0 {
            sum += num % 10
            num /= 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



