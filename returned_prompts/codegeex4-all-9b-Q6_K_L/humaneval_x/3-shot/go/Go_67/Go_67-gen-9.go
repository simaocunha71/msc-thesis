    var apples int
    var oranges int
    appleStr := strings.Split(s, "apples and")
    orangesStr := strings.Split(appleStr[1], "oranges")
    apples, _ = strconv.Atoi(appleStr[0])
    oranges, _ = strconv.Atoi(orangesStr[0])
    return n - apples - oranges
}



