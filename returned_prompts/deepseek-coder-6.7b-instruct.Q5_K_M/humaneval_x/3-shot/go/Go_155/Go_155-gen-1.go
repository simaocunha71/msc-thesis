    numStr := strconv.Itoa(int(math.Abs(float64(num))))
    evenCount := 0
    oddCount := 0

    for _, digitChar := range numStr {
        digit, _ := strconv.Atoi(string(digitChar))
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }

    return [2]int{evenCount, oddCount}
}



