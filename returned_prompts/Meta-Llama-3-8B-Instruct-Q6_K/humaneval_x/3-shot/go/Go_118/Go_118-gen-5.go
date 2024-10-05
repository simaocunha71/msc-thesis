    var closestVowel string
    var closestDistance int

    for i := len(word) - 1; i >= 0; i-- {
        c := word[i]
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            if closestVowel == "" || i - closestDistance > i {
                closestVowel = string(c)
                closestDistance = i
            }
        }
    }
    return closestVowel
}