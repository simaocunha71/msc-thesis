    var bored int
    pattern := regexp.MustCompile(`(?i)I(.*?)\.|I(.*?)\?|I(.*?)!`)
    bored = len(pattern.FindAllString(S, -1))
    return bored
}