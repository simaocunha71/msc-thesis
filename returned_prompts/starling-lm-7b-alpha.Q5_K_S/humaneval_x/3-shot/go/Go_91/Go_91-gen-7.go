    regex := regexp.MustCompile(`\bI\s+[a-z]*[.?!]`)
    return regex.FindStringSubmatch(S) != nil
}



