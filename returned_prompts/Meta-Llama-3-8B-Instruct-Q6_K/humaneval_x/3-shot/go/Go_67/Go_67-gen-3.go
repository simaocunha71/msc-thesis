    words := strings.Split(s, " ")
    count := 0
    for _, word := range words {
        if strings.Contains(word, "apples") {
            count, _ = strconv.Atoi(strings.Replace(word, "apples", "", -1))
        } else if strings.Contains(word, "oranges") {
            count, _ = strconv.Atoi(strings.Replace(word, "oranges", "", -1))
        }
    }
    return n - count
}