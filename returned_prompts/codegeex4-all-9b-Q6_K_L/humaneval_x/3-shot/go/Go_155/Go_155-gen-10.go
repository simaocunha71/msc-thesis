    var evenCount, oddCount int
    strNum := strconv.Itoa(num)

    for _, c := range strNum {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}



