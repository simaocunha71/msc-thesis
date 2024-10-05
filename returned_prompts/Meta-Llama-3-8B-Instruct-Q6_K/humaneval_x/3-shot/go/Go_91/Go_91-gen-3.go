    re, _ := regexp.Compile(`^I.*[.!?]`)
    matches := re.FindAllString(S, -1)
    return len(matches)
}