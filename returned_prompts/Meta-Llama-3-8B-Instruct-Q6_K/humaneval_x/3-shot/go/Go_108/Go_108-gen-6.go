    var count int
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        total := 0
        for num > 0 {
            digit := num % 10
            total += digit
            num /= 10
        }
        if total > 0 {
            count++
        }
    }
    return count
}