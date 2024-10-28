    re := regexp.MustCompile(`(?i)\bI\w*[.?!]`)
    matches := re.FindAllString(S, -1)
    return len(matches)
}



