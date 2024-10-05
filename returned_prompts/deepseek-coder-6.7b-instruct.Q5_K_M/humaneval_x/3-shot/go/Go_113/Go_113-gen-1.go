    result := make([]string, len(lst))
    for i, str := range lst {
        count := 0
        for _, ch := range str {
            if (ch - '0') % 2 != 0 {
                count += 1
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, i, count)
    }
    return result
}



