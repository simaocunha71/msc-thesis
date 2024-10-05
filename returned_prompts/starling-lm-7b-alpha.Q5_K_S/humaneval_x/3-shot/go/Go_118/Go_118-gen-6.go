    const vowels = "aeiouAEIOU"

    for i := len(word) - 2; i >= 0; i-- {
        if !contains(vowels, word[i]) {
            continue
        }
        if contains(vowels, word[i-1]) {
            continue
        }
        return string(word[i])
    }
    return ""
}

func contains(haystack string, needle string) bool {
    index := bytes.IndexByte(haystack, needle[0])
    return index != -1
}



