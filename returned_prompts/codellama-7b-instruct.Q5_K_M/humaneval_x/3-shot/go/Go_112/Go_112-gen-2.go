    result := make([]rune, 0)
    for _, c := range s {
        if !strings.Contains(c, string(c)) {
            result = append(result, c)
        }
    }
    return [2]interface{}{string(result),strings.Contains(string(result), string(result[len(result)-1]))}
}



