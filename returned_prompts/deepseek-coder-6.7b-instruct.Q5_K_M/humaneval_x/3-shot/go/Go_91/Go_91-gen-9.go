    re := regexp.MustCompile(`(?i)^I.*[.?!]`)
    sentences := re.FindAllString(S, -1)
    return len(sentences)
}

