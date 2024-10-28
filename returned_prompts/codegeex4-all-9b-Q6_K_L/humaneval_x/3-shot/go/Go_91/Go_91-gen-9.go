    re := regexp.MustCompile(`I[\w\s]*[.?!]`)
    return len(re.FindAllString(S, -1))
}



