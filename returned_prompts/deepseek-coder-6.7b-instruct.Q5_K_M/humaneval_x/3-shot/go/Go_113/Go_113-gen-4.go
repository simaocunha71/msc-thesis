    result := make([]string, len(lst))

    for i, str := range lst {
        count := 0
        for _, c := range str {
            if int(c-'0') % 2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", count, string(count+'0'), count, count)
    }
    return result
}



