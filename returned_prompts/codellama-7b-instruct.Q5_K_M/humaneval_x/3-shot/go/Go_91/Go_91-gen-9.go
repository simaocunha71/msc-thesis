    var count int = 0
    reg, _ := regexp.Compile("I")
    match := reg.FindAllString(S, -1)
    count = len(match)
    return count
}



