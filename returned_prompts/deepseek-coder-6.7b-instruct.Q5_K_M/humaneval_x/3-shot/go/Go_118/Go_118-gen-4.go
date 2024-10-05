    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    var closestVowel string
    for i := len(word) - 1; i > 0; i-- {
        if !bytes.ContainsRune([]byte(vowels), rune(word[i])) && bytes.ContainsRune([]byte(vowels), rune(word[i-1])) && bytes.ContainsRune([]byte(vowels), rune(word[i+1])) {
            closestVowel = string(word[i])
            break
        }
    }
    return closestVowel
}


