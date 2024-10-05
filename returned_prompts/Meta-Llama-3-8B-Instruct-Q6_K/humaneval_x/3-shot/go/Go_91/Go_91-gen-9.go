    re, _ := regexp.Compile(`^I`)
    return len(re.FindAllString(S, -1))
}