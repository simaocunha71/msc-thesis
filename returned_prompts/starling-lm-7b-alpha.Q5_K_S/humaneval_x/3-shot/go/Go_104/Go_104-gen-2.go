    result := make([]int, 0)
    for _, v := range x {
        if !hasEvenDigit(v) {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}

func hasEvenDigit(n int) bool {
    for _, v := range strconv.Itoa(n) {
        if digit, _ := strconv.Atoi(string(v)); digit%2 == 0 {
            return true
        }
    }
    return false
}



