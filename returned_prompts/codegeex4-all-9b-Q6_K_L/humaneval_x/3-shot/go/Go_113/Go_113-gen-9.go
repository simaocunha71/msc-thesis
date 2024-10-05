    result := make([]string, 0)
    for _, s := range lst{
        var count int = 0
        for _, c := range s {
            if c % 2 == 1 {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, count, count))
    }
    return result
}

