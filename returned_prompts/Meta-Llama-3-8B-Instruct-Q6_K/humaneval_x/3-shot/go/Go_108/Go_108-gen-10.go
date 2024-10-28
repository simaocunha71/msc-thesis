    count := 0
    for _, num := range arr {
        numStr := strconv.FormatInt(int64(num), 10)
        if num < 0 {
            numStr = numStr[1:]
        }
        sum := 0
        for _, c := range numStr {
            sum += int(c - '0')
        }
        if sum > 0 {
            count++
        }
    }
    return count
}