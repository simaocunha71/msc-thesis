    result := make([]string, 0)
    for i := 0; i < len(lst); i++ {
        odd_count := 0
        for _, c := range lst[i] {
            if c - '0' % 2 != 0 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %d in the string %d of the input.", odd_count, i))
    }
    return result
}



