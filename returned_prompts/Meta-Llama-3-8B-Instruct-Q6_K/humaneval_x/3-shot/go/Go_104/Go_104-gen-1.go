    result := make([]int, 0)
    for _, num := range x {
        str := strconv.Itoa(num)
        has_even_digit := false
        for _, c := range str {
            digit, _ := strconv.Atoi(string(c))
            if digit%2==0 {
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