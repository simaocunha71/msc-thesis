    result := make([]string, 0)
    for _, s := range lst {
        odd_count := 0
        for _, c := range s {
            if (c-'0') % 2 != 0 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %d%snput.", odd_count, s, odd_count, odd_count, s))
    }
    return result
}



