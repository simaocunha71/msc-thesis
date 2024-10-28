    result := make([]rune, 0)
    for _, c := range s {
        var index int = strings.IndexRune("abcdefghijklmnopqrstuvwxyz", c)
        if index == -1 {
            result = append(result, c)
        } else {
            if index >= 20 {
                result = append(result, rune('a' + (index % 20)))
            } else {
                result = append(result, rune('a' + (index * 2)))
            }
        }
    }
    return string(result)
}



