    parts := strings.Split(s," ")
    apples, _ := strconv.Atoi(strings.Split(parts[0]," ")[0])
    oranges, _ := strconv.Atoi(strings.Split(parts[1]," ")[0])
    return n - apples - oranges
}