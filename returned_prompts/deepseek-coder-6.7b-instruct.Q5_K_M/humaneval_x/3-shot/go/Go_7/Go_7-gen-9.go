    result := make([]string, 0)

    for _, value := range stringList {
        if strings.Contains(value, substring) {
            result = append(result, value)
        }
    }

    return result
}



