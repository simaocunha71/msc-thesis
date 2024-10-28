    var result []int
    for _, num := range x {
        s := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range s {
            if c % 2 == 0 {
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