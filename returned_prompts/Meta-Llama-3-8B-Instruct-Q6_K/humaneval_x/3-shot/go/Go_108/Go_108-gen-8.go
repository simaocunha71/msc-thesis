    count := 0
    for _, num := range arr {
        if num < 0 {
            num = -num
        }
        sum := 0
        for _, digit := range strconv.Itoa(int(num)) {
            sum += int(digit - '0')
        }
        if sum > 0 {
            count++
        }
    }
    return count
}