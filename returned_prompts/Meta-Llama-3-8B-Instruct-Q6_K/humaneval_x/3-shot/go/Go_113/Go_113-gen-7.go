    result := make([]string, 0)
    for _, s := range lst {
        count := 0
        for _, c := range s {
            if c % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, 1+len(result), 1+len(result), 1+len(result)))
    }
    return result
}