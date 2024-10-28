    result := make([]string, len(lst))
    for i := range lst {
        count := 0
        for _, v := range lst[i] {
            if v % 2 != 0 {
                count += 1
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%rng %d of the %dnput.", count, len(lst[i]), i, len(lst))
    }
    return result
}



