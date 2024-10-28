    parts := strings.Split(s," ")
    apples, _ := strconv.Atoi(parts[0][0:len(parts[0])-5])
    oranges, _ := strconv.Atoi(parts[1][0:len(parts[1])-5])
    total := apples + oranges
    return n - total
}




