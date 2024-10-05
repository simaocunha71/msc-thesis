    result := make([]string, len(lst))

    for i := 0; i < len(lst); i++ {
        count := 0
        for _, c := range lst[i] {
            if (int(c-'0'))%2 == 1 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", count, count, count, count)
    }
    return result
}



