    filtered := []string{}
    for _, s := range stringList {
        if strings.Contains(s, substring) {
            filtered = append(filtered, s)
        }
    }
    return filtered
}



