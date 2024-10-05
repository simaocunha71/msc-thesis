    result := make([]string, 0)

    for _, s := range lst {
        count := 0
        for _, c := range s {
            if int(c)-48 % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, 48+len(s), 48+len(s), 48+len(s)))
    }
    return result
}