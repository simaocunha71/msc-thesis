    result := make([]string, 0)
    for _, str := range lst {
        count := 0
        for _, c := range str {
            if c % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dn of the %dnput.", count, len(str), len(str)))
    }
    return result
}