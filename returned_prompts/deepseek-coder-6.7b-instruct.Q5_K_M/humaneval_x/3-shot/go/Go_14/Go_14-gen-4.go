    prefixes := make([]string, 0, len(str))
    for i := 0; i < len(str); i++ {
        prefixes = append(prefixes, str[:i+1])
    }
    return prefixes
}



