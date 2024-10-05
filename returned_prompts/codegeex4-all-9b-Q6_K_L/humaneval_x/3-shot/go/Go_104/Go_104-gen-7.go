    result := make([]int, 0)
    for _, i := range x {
        is_even := false
        for _, digit := range strconv.Itoa(i) {
            if digit%2 == 0 {
                is_even = true
                break
            }
        }
        if !is_even {
            result = append(result, i)
        }
    }
    sort.Ints(result)
    return result
}