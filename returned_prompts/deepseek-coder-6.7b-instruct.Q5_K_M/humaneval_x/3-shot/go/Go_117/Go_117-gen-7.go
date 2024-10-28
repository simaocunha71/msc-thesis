    var result []string
    words := strings.Fields(s)
    for _, word := range words {
        count := 0
        for _, c := range word {
            c := bytes.ToLower([]byte{byte(c)})[0]
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}



