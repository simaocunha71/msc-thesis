    var apples int
    var oranges int
    var mango int

    var fruit []string
    fruit = strings.Split(s, " ")

    apples, _ = strconv.Atoi(fruit[0])
    oranges, _ = strconv.Atoi(fruit[2])

    mango = n - apples - oranges

    return mango
}



