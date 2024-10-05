    result := make([]rune, 0)
    for _, group := range strings.Split(s, "") {
        if len(group) == 2 {
            result = append(result, rune(group[0]))
            result = append(result, rune(group[1]))
            result = append(result, rune(group[0]))
        } else {
            for _, c := range group {
                result = append(result, c)
            }
        }
    }
    return string(result)
}