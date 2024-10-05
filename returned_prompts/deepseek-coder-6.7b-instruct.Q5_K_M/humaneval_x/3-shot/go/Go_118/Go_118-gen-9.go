    var vowels = []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    var vowelFound = false
    var closestVowel = ""

    for i := len(word) - 1; i >= 1; i-- {
        if bytes.ContainsRune([]byte(vowels), rune(word[i])) {
            vowelFound = true
        }
        if vowelFound && !bytes.ContainsRune([]byte(vowels), rune(word[i-1])) && !bytes.ContainsRune([]byte(vowels), rune(word[i+1])) {
            closestVowel = string(word[i])
            break
        }
    }

    return closestVowel
}



