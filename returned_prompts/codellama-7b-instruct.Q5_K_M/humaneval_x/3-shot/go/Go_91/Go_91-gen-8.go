    re := regexp.MustCompile(`I\s+`)
    count := 0
    for _, match := range re.FindAllString(S, -1) {
        count += 1
    }
    return count
}



