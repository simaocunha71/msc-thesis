    var result []string
    words := strings.Split(s, " ")
    for _, word := range words {
        count := 0
        for _, c := range word {
            if bytes.ContainsRune([]byte("aeiouAEIOU "), c) {
                continue
            }
            count++
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



