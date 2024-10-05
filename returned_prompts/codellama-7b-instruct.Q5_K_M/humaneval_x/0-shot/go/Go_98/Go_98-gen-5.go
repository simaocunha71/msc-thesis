    for _, r := range strings.ToUpper(s) {
        if strings.Contains("AEIOU", string(r)) {
            continue A
        }
    }
    return 0
}

