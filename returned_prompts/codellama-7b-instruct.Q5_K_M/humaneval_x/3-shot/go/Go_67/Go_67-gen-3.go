    var apples int
    var oranges int

    s1 := strings.Split(s, " ")
    apples, _ = strconv.Atoi(s1[0])
    oranges, _ = strconv.Atoi(s1[2])

    return n - apples - oranges
}



