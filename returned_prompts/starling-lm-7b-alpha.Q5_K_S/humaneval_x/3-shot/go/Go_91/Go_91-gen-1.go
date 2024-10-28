    r := regexp.MustCompile(`(?i)i\s.*\.[?.!]`)
    return len(r.FindAllString(S, -1))
}



