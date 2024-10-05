    result := make([]string, 0, len(lst))
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if (c-'0') % 2 == 1 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, i, i))
    }
    return result
}


