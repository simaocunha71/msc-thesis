    count := 0
    for _, num := range arr {
        sum := 0
        str := strconv.Itoa(num)
        for _, ch := range str {
            digit, _ := strconv.Atoi(string(ch))
            sum += digit
        }
        if sum > 0 {
            count += 1
        }
    }
    return count
}


