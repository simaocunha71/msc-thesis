    result := make([]string, 0)
    for _, s := range lst {
        odd_count := 0
        for _, c := range s {
            if c - '0' % 2 != 0 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %d in the string %s of the input.", odd_count, s))
    }
    return result
}



