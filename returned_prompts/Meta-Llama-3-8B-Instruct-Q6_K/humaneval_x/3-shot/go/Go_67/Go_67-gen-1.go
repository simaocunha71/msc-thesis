    words := strings.Split(s, " ")
    count_apples, _ := strconv.Atoi(strings.Split(words[1], " ")[0])
    count_oranges, _ := strconv.Atoi(strings.Split(words[3], " ")[0])
    return n - count_apples - count_oranges
}

