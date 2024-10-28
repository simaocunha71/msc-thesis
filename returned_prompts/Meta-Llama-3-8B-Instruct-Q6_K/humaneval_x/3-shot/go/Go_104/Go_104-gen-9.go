    var result []int
    for _, num := range x {
        str := strconv.Itoa(num)
        hasEvenDigit := false
        for _, c := range str {
            if _, err := strconv.Atoi(string(c)); err == nil && c-'0' % 2 == 0 {
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