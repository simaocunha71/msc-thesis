    count := 0
    for _, num := range arr {
        sum := 0
        numStr := strconv.Itoa(num)
        for _, ch := range numStr {
            digit, _ := strconv.Atoi(string(ch))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



