    for _, value := range dict {
        _, ok := value.(string)
        if !ok {
            return false
        }
    }

    if len(dict) == 0 {
        return false
    }

    firstKey := ""
    for key := range dict {
        firstKey = key.(string)
        break
    }

    return strings.ToLower(firstKey) == firstKey || strings.ToUpper(firstKey) == firstKey
}



