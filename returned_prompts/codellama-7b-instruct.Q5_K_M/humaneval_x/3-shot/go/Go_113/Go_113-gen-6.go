    var result []string

    for i, v := range lst {
        var count int
        for _, c := range v {
            if c == '1' {
                count += 1
            }
        }
        result = append(result, fmt.Sprintf("the number of odd elements %v in the str%vng %v of the %vnput.", count, len(v), i, len(v)))
    }

    return result
}



