    result := make([]string, 0)
    for _, v := range stringList {
        if strings.Contains(v, substring) {
            result = append(result, v)
        }
    }
    return result
}



