    result := make([]string, 0)
    for _, str := range lst {
        count := 0
        for _, c := range str {
            if c%2 == 1 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%ng %d of the %dnput.", count, count, count, count))
    }
    return result
}



