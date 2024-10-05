    var evenCount int
    var oddCount int

    numStr := strconv.Itoa(num)
    for _, c := range numStr {
        if c-'0' % 2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}