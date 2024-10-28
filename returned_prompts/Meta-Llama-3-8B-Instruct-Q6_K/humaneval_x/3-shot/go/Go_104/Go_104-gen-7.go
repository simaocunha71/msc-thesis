    var result []int
    for _, num := range x {
        digits := []rune(strconv.Itoa(num))
        hasEvenDigit := false
        for _, digit := range digits {
            if digit % 2 == 0 {
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





