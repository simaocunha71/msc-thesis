    vowels := []byte("aeiouAEIOU")
    for i := len(word) - 1; i >= 0; i-- {
        if bytes.IndexByte(vowels, word[i]) >= 0 {
            for j := i - 1; j >= 0; j-- {
                if !bytes.IndexByte(vowels, word[j]) >= 0 {
                    return string(word[i])
                }
            }
        }
    }
    return ""
}