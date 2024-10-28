    var result []int
    for _, v := range x {
        str := strconv.Itoa(v)
        hasEvenDigit := false
        for _, c := range str {
            if d, err := strconv.Atoi(string(c)); err == nil && d%2 == 0 {
                hasEvenDigit = true
                break
            }
        }
        if !hasEvenDigit {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
}