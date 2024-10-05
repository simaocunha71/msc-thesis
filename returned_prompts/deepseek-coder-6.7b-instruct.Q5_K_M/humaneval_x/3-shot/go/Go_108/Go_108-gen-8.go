    count := 0
    for _, num := range arr {
        sum := 0
        for _, digit := range strconv.Itoa(num) {
            if digit == '-' {
                continue
            }
            intDigit, _ := strconv.Atoi(string(digit))
            sum += intDigit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



