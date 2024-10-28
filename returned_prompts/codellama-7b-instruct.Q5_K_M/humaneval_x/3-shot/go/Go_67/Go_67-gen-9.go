    var apples int
    var oranges int

    s_split := strings.Split(s," ")
    apples,_ = strconv.Atoi(s_split[0])
    oranges,_ = strconv.Atoi(s_split[2])

    return n - apples - oranges
}



