    words := strings.Split(s," ")
    count_apples, _ := strconv.Atoi(strings.Split(words[2]," ")[0])
    count_oranges, _ := strconv.Atoi(strings.Split(words[4]," ")[0])
    return n - count_apples - count_oranges
}