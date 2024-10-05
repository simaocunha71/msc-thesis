    for _, value := range dict {
        if _, ok := value.(string); !ok {
            return false
        }
    }

    allLower := true
    allUpper := true

    for key := range dict {
        keyStr, ok := key.(string)
        if !ok {
            return false
        }

        if strings.ToLower(keyStr) != keyStr {
            allLower = false
        }
        if strings.ToUpper(keyStr) != keyStr {
            allUpper = false
        }
    }

    return allLower || allUpper
}



