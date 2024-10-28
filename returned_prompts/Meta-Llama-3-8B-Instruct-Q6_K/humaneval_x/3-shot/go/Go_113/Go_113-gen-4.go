    result := make([]string, 0)
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if c % 2 != 0 {
                count++
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the string %d of the input.", count, i+1))
    }
    return result
}