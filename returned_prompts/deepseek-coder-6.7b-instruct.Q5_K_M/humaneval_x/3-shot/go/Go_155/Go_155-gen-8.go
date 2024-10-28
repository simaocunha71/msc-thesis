    evenCount := 0
    oddCount := 0
    numStr := strconv.Itoa(int(math.Abs(float64(num))))

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



