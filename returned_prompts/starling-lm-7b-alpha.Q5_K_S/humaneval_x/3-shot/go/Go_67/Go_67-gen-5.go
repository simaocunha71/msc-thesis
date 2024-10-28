    parts := strings.Split(s, " and ")
    apples, _ := strconv.Atoi(parts[0][2:])
    oranges, _ := strconv.Atoi(parts[1][0:len(parts[1])-1])
    return n - apples - oranges
}




