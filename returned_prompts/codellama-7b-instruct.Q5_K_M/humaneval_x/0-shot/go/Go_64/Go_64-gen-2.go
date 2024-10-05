    for _, c := range s {
        switch strings.ToLower(string(c)) {
        case "a", "e", "i", "o", "u":
            continue A
        }
    }

    return 0
}
