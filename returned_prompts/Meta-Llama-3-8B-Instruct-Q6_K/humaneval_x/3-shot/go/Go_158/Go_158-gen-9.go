    var max_word string
    var max_unique_chars int
    for _, word := range words {
        unique_chars := len([]rune(strings.Map(func(r rune) rune {
            if strings.Contains(string(r), string(r)) {
                return -1
            }
            return r
        }, word)))
        if unique_chars > max_unique_chars {
            max_unique_chars = unique_chars
            max_word = word
        }
    }
    return max_word
}  // this function can be optimized by using a map to count unique characters of each word and then find the max. But for simplicity, the current version is implemented.