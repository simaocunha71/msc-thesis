    regex := regexp.MustCompile(`I\s[^.?!]+[.?!]`)
    return len(regex.FindAllString(S, -1))
}



