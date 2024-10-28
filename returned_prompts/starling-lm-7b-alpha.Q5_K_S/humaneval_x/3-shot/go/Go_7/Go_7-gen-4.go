    result := make([]string, 0)
    for _, stringValue := range stringList {
        if strings.Contains(stringValue, substring) {
            result = append(result, stringValue)
        }
    }
    return result
}



