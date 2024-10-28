    result := make([]string, 0)
    for _, s := range lst {
        odd_count := 0
        for _, c := range s {
            if c % 2 != 0 {
                odd_count += 1
            }
        }

        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", odd_count, s, odd_count, len(lst)))
    }
    return result
}



