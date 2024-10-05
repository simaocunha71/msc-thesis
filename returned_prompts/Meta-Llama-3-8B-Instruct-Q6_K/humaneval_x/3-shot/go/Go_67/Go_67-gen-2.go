    words := strings.Split(s, " ")
    apples, _ := strconv.Atoi(strings.Split(words[1], " ")[0])
    oranges, _ := strconv.Atoi(strings.Split(words[3], " ")[0])
    return n - apples - oranges
}