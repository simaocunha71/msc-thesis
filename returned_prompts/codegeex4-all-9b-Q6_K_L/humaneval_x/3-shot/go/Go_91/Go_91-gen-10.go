    var count = 0
    r := regexp.MustCompile(`(?i)(^I\w*\.|\?I\w*\.|!I\w*\.|\?I\w*!|!I\w*!)`)
    matches := r.FindAllString(S, -1)
    count = len(matches)
    return count
}

