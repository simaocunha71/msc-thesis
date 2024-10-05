    strSlice := strings.Split(s," ")
    apples, _ := strconv.Atoi(strSlice[2])
    oranges, _ := strconv.Atoi(strSlice[6])
    return n - apples - oranges
}



