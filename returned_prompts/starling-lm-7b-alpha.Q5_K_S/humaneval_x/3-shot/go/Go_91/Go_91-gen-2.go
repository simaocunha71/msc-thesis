    regex := regexp.MustCompile(`^I\s*[?.!]`)
    return regex.FindStringSubmatch(S) != nil
}



