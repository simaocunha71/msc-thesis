    words := strings.Split(s, " ")
    consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result := make([]string, 0)

    for _, word := range words {
        count := 0
        for _, letter := range word {
            if strings.ContainsRune(consonants, letter) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}

In the solution above, I added the upper case letters in the "consonants" string to handle the case when the input string contains upper case letters as well.

