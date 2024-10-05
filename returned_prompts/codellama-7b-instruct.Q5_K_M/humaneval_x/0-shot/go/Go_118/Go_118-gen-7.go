for i := len(word) - 2; i >= 0; i-- {
    if isVowel(word[i]) {
        return word[i : i+1]
    }
    if !isConsonant(word[i]) {
        continue A
    }
    for j := i + 2; j < len(word); j++ {
        if isVowel(word[j]) {
            return word[j : j+1]
        }
        if !isConsonant(word[j]) {
            continue A
        }
    }
}
return ""
}

func isVowel(ch byte) bool {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
}

func isConsonant(ch byte) bool {
    return ch >= 'A' && ch <= 'Z' && !isVowel(ch)
}


