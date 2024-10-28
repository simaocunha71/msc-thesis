    re := regexp.MustCompile(`\bI\s*\b`)
    return len(re.FindAllString(S, -1))
}



