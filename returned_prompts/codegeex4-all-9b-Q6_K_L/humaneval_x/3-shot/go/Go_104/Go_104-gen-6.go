    result := make([]int, 0)
    for _, number := range x {
        has_even := false
        for _, digit := range strconv.Itoa(number) {
            if digit%2 == 0 {
                has_even = true
                break
            }
        }
        if !has_even {
            result = append(result, number)
        }
    }
    sort.Ints(result)
    return result
}



