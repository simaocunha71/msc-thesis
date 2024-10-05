    result := make([]string, 0)
    for _, str := range lst {
        count := 0
        for _, digit := range str {
            if digit%2 != 0 {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.", count, str, count, len(lst)))
    }
    return result
}



