func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, s := range lst {
        oddCount := 0
        for _, c := range s {
            if (c - '0') % 2 == 1 {
                oddCount++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", oddCount, oddCount, oddCount, oddCount)
    }
    return result
}

