    var result []int
    for _, num := range x {
        digits := []rune(strconv.Itoa(num))
        has_even_digit := false
        for _, digit := range digits {
            if digit%2 == 0 {
                has_even_digit = true
                break
            }
        }
        if !has_even_digit {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}