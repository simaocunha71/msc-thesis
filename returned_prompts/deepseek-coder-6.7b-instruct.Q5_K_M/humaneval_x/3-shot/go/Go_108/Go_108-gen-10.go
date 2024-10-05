    count := 0
    for _, num := range arr {
        sum := 0
        for _, digit := range strconv.Itoa(num) {
            digitValue, _ := strconv.Atoi(string(digit))
            sum += digitValue
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



