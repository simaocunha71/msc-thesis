    var evenCount int = 0
    var oddCount int = 0

    for _, c := range strconv.Itoa(num) {
        if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
            evenCount += 1
        } else {
            oddCount += 1
        }
    }
    return [2]int{evenCount, oddCount}
}