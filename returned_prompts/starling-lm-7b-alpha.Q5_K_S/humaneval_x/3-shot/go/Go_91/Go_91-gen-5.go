    result := 0
    regexp := regexp.MustCompile(`I\s.*\.|\?|\!`)
    if regexp.MatchString(S) {
        result += 1
    }
    return result
}



