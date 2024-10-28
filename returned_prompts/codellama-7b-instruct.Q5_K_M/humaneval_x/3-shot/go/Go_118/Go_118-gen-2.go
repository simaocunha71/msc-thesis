    var vowels = []byte{'a', 'e', 'i', 'o', 'u'}
    var is_vowel = func(c byte) bool {
        for _, v := range vowels {
            if v == c {
                return true
            }
        }
        return false
    }

    var is_consonant = func(c byte) bool {
        return !is_vowel(c)
    }

    var buffer = bytes.Buffer{}

    for i := len(word) - 1; i >= 0; i-- {
        c := word[i]

        if is_consonant(c) {
            buffer.WriteByte(c)
        } else if is_vowel(c) {
            if buffer.Len() > 0 {
                buffer.Reset()
            } else {
                return string(c)
            }
        }
    }
    return ""
}


