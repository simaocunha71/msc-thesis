    re := regexp.MustCompile(`(?i)i\s`)
    return len(re.FindAllStringIndex(S, -1))
}



