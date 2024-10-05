    var count int
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        for num > 0 {
            digit, _ := strconv.Atoi(string(rune(num % 10)))
            sum += digit
            num /= 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
} 



