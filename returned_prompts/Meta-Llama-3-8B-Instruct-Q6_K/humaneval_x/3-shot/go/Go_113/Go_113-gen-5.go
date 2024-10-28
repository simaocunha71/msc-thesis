    result := make([]string, 0)
    for _, s := range lst {
        odd_count := 0
        for _, c := range s {
            if c % 2 != 0 {
                odd_count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dc of the %dnput.", odd_count, len(s), len(s)))
    }
    return result
}