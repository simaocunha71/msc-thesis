    var vowels = []byte{'a','e','i','o','u'}
    var consonants = []byte{'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
    var closest_vowel byte
    var found bool

    var word_bytes = []byte(word)

    for i := len(word_bytes) - 2; i >= 0; i-- {
        if bytes.Index(consonants,word_bytes[i]) != -1 {
            for _, vowel := range vowels {
                if bytes.Index(vowels,word_bytes[i+1]) == -1 && vowel == word_bytes[i+1] {
                    found = true
                    closest_vowel = vowel
                    break
                }
            }
            if found {
                break
            }
        }
    }
    if found {
        return string(closest_vowel)
    }
    return ""
}



