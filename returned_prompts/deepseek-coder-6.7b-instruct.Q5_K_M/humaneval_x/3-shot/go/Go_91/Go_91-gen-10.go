    re := regexp.MustCompile(`\bI[^.]*\.`)
    matches := re.FindAllString(S, -1)
    return len(matches)
}



