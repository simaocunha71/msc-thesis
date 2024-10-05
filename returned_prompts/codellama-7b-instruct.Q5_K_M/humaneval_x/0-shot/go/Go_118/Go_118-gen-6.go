    // Find the index of the last consonant
    for i := len(word) - 1; i >= 0; i-- {
        if bytes.IndexByte([]byte(Consonants), word[i]) == -1 {
            continue
        }

        // Find the index of the first vowel from the left
        for j := i - 1; j >= 0; j-- {
            if bytes.IndexByte([]byte(Vowels), word[j]) != -1 {
                return word[j : i+1]
            }
        }

        // If we are still at the last consonant, return empty string
        continue A
    }

    return ""
}
