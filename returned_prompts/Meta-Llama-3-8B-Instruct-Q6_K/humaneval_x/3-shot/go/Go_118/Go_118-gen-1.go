    vowels := "aeiouAEIOU"
    for i := len(word) - 1; i > 0; i-- {
        if bytes.IndexByte([]byte(vowels), byte(word[i])) != -1 {
            return string(word[i])
        }
    }
    return ""
}
} 

