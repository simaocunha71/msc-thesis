    result := make([]string, 0, len(lst))

    for _, str := range lst {
        count := 0
        for _, ch := range str {
            if int(ch-'0') % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", count, "%", count, count))
    }

    return result
}



