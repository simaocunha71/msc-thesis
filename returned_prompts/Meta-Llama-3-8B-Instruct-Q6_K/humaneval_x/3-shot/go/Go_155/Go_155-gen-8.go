    var evenCount int = 0
    var oddCount int = 0
    numStr := strconv.Itoa(num)
    for _, c := range numStr {
        digit, _ := strconv.Atoi(string(c))
        if digit % 2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}