    prefixes := make([]string, 0)
    for i := 0; i < len(str); i++ {
        prefixes = append(prefixes, str[:i+1])
    }
    return prefixes
}



