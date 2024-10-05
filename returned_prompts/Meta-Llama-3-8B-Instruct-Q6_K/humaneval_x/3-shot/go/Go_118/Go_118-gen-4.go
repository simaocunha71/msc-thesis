    var closestVowel rune
    var minDistance int
    for i := len(word) - 1; i >= 0; i-- {
        c := word[i]
        if "AEIOUaeiou"[c-'a'] >= 0 {
            if closestVowel == 0 || i - closestVowel < minDistance {
                closestVowel = i
                minDistance = i - closestVowel
            }
        }
    }
    if closestVowel > 0 {
        return string(word[closestVowel])
    } else {
        return ""
    }
}