    var result []string
    words := bytes.Split([]byte(s), []byte(" "))
    for _, word := range words {
        word = bytes.TrimSpace(word)
        word = []byte(strings.ToLower(string(word)))
        count := 0
        for _, c := range word {
            if c >= 'a' && c <= 'z' {
                if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' {
                    count++
                }
            }
        }
        if count == n {
            result = append(result, string(word))
        }
    }
    return result
}