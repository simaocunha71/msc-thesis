    count := 0
    for _, number := range arr {
        sum := 0
        strNum := strconv.Itoa(number)
        for _, char := range strNum {
            intChar, _ := strconv.Atoi(string(char))
            sum += intChar
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



