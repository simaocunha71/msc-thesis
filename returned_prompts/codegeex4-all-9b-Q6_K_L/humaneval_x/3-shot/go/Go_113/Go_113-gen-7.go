    result := make([]string, 0)
    for _, string := range lst {
        odd_count := 0
        for _, digit := range string {
            if digit%2 != 0 {
                odd_count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", odd_count, odd_count, odd_count, odd_count))
    }
    return result
}