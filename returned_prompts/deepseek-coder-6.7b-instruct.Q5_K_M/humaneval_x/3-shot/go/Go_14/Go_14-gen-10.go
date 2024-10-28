    prefixes := make([]string, len(str))
    for i := range str {
        prefixes[i] = str[:i+1]
    }
    return prefixes
}



