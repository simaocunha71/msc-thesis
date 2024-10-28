    var result []string
    words := strings.Split(s, " ")

    for _, word := range words {
        count := 0
        for _, letter := range word {
            if strings.ContainsRune("aeiouAEIOU", letter) == false {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



