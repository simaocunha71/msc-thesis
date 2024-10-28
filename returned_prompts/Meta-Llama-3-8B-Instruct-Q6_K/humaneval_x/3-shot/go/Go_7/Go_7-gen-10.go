    result := make([]string, 0)
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
} 



