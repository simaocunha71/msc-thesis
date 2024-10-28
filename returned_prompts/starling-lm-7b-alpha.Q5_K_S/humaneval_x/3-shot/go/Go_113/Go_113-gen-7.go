    result := make([]string, 0)
    for _, str := range lst {
        odd_count := 0
        for _, char := range str {
            if char%2 == 1 {
                odd_count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", odd_count, string(str[len(str)-1]), odd_count, len(str)))
    }
    return result
}



