    var re = regexp.MustCompile(`(?i)^i`)
    words := re.FindAllStringIndex(S, -1)
    return len(words)
}



