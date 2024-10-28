    result := []rune{}

    for _, char := range s {
        if !strings.Contains(c, string(char)) {
            result = append(result, char)
        }
    }

    if len(result) == 0 {
        return []interface{}{string(result), false}
    }
    return []interface{}{string(result), result == strings.Join(strings.Split(string(result), ""), "")}
}



