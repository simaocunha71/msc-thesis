    for i := len(word) - 2; i > 0; i-- {
        if !isVowel(word[i]) && isConsonant(word[i-1]) && isConsonant(word[i+1]) {
            for _, v := range "aeiouAEIOU" {
                if bytes.ContainsRune([]rune(word[i-1:i+2]), v) {
                    return string(v)
                }
           