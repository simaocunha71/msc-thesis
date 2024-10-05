    result := make([]int, 0)
    for i := 0; i < len(x); i++ {
        is_even := false
        for _, c := range strconv.Itoa(x[i]) {
            if c == '0' || c == '2' || c == '4' || c == '6' || c == '8' {
                is_even = true
                break
            }
        }
        if !is_even {
            result = append(result, x[i])
        }
    }
    sort.Ints(result)
    return result
}