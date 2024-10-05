    var result []int
    for _, num := range x {
        var hasEvenDigit bool
        numStr := strconv.Itoa(num)
        for _, c := range numStr {
            digit, _ := strconv.Atoi(string(c))
            if digit%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}