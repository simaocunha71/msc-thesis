    vowels := "aeiouAEIOU"
    closest_vowel := ""
    for i := len(word)-1; i > 0; i-- {
        if closest_vowel == "" && string(word[i]) != "" && !strings.Contains(vowels, string(word[i])) {
            if strings.Contains(vowels, string(word[i-1])) {
                closest_vowel = string(word[i-1])
            }
        }
        if string(word[i]) == "" && closest_vowel != "" {
            break
        }
    }
    return closest_vowel
}



