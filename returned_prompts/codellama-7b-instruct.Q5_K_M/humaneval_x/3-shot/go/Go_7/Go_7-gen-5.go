    result := make([]string, 0)
    substring = strings.ToLower(substring)

    for _, s := range stringList {
        if strings.Contains(strings.ToLower(s), substring) {
            result = append(result, s)
        }
    }
    return result
}



