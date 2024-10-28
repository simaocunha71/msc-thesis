    result := 0
    regex := "^I.*[.?!]$"

    match := regexp.MustCompile(regex).FindStringSubmatch(S)
    for match != nil {
        result += 1
        match = regexp.MustCompile(regex).FindStringSubmatch(S)
    }

    return result
}



