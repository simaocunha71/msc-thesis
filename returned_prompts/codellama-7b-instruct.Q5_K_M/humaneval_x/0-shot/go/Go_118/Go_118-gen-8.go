for i := len(word) - 1; i >= 0; i-- {
    if IsVowel(word[i]) {
        if i == len(word) - 1 {
            continue A
        }
        for j := i + 1; j < len(word); j++ {
            if IsConsonant(word[j]) {
                return string(word[i])
            }
        }
    }
}
return ""
}

func IsConsonant(c byte) bool {
    if bytes.IndexByte("bcdfghjklmnpqrstvwxyz", c) >= 0 {
        return false
    }
    return true
}

func IsVowel(c byte) bool {
    if bytes.IndexByte("aeiou", c) >= 0 {
        return true
    }
    return false
}


