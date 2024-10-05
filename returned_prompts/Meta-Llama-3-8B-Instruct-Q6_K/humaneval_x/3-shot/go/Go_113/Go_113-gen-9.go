    result := make([]string, 0)
    for _, str := range lst {
        odd_count := 0
        for _, c := range str {
            if c % 2 != 0 {
                odd_count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the string %s of the input.", odd_count, str))
    }
    return result
}