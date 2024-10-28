    words := strings.Split(s," ")
    apple_count := 0
    for _, word := range words {
        if strings.HasPrefix(word, "apples") {
            count, _ := strconv.Atoi(strings.Replace(word, "apples", "", -1))
            apple_count = count
        }
    }
    return n - apple_count
}