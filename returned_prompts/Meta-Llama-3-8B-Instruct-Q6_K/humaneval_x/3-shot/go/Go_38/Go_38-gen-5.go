    result := make([]rune, 0)
    for _, c := range s {
        if len(result) > 0 {
            result = append([]rune{result[0]}, result[1:]...)
        }
        result = append(result, c)
    }
    return string(result)
}