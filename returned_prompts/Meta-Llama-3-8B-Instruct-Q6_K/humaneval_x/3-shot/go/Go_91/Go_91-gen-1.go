    regex, _ := regexp.Compile(`^I.*[.!?]`)
    return len(regex.FindAllString(S, -1))
} 



