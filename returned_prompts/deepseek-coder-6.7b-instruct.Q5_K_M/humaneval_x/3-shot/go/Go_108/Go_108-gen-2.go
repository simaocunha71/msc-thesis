    count := 0
    for _, num := range arr {
        sum := 0
        strNum := strconv.Itoa(num)
        for _, char := range strNum {
            digit, _ := strconv.Atoi(string(char))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



