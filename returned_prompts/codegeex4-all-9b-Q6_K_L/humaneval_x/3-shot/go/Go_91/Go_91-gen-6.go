    pattern := regexp.MustCompile(`(?<=I\s)[^.?!]*`)
    matches := pattern.FindAllString(S, -1)
    return len(matches)
}



