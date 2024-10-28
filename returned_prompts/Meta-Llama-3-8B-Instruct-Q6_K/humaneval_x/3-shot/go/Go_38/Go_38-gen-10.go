    result := make([]rune, 0)
    for _, group := range strings.Split(s, "") {
        runes := []rune(group)
        if len(group) == 2 {
            result = append(result, runes[0], runes[1], rune(0))
        } else {
            result = append(result, runes...)
        }
    }
    return string(result)
}