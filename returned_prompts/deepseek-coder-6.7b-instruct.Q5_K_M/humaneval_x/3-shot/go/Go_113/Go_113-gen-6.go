    res := make([]string, len(lst))
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if int(c-'0') % 2 != 0 {
                count++
            }
        }
        res[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, i, i)
    }
    return res
}


