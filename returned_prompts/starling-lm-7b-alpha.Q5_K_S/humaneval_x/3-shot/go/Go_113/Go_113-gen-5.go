    result := make([]string, 0)
    for _, i := range lst {
        odd_count := 0
        for _, j := range i {
            if int(j) % 2 != 0 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", odd_count, i, odd_count, len(lst)))
    }
    return result
}



