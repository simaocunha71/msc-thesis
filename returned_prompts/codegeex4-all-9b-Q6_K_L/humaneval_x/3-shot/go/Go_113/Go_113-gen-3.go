    result := make([]string, 0)
    for _, s := range lst {
        odd_count := 0
        for _, c := range s {
            if (c - '0') % 2 == 1 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", odd_count, odd_count, odd_count, odd_count))
    }
    return result
}



