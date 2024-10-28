    result := make([]int, 0)

    for _, num := range x {
        hasEvenDigit := false
        for _, digit := range strconv.Itoa(num) {
            digitInt, _ := strconv.Atoi(string(digit))
            if digitInt % 2 == 0 {
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



