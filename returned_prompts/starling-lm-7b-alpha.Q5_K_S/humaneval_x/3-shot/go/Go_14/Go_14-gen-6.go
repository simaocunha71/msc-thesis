    result := make([]string, 0)

    for length := 1; length <= len(str); length++ {
        result = append(result, str[:length])
    }

    return result
}



