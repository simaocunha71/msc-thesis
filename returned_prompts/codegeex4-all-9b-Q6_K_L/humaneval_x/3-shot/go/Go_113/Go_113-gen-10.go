    result := make([]string, 0)

    for _, string := range lst {
        odd_count := 0
        for _, c := range string {
            if (c-'0')%2 == 1 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%dgng %d of the %dnput.", odd_count, odd_count, odd_count, odd_count))
    }
    return result
}

