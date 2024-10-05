    re := regexp.MustCompile(`^I\w+`)
    return len(re.FindAllStringIndex(S, -1))
}



