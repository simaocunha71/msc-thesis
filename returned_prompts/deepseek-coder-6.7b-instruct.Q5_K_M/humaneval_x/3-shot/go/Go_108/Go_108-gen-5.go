    count := 0
    for i := 0; i < len(arr); i++ {
        sum := 0
        str := strconv.Itoa(arr[i])
        for _, c := range str {
            if c == '-' {
                continue
            }
            digit, _ := strconv.Atoi(string(c))
            sum += digit
        }
        if sum > 0 {
            count++
        }
    }
    return count
}



