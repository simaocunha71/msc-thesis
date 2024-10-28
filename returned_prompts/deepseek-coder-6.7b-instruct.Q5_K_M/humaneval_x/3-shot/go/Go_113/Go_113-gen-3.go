    result := make([]string, 0)
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if (c - '0') % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, i, i))
    }
    return result
}



