    var apples,oranges int
    var tokens = strings.Split(s, " ")
    for i,token := range tokens {
        if i%2==0 {
            apples, _ = strconv.Atoi(token)
        } else {
            oranges, _ = strconv.Atoi(token)
        }
    }
    return n - apples - oranges
}




