    re := regexp.MustCompile("I.+?[.?!]")
    return len(re.FindAllString(S, -1))
}



