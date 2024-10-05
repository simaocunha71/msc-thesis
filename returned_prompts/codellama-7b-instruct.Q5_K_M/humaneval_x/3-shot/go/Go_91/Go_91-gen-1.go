    pattern := regexp.MustCompile("I.*[.?!]")
    return len(pattern.FindAllString(S, -1))
}




