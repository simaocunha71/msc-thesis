    if len(words) == 0 {
        return ""
    }
    sort.Slice(words, func(i, j int) bool {
        if len(words[i]) == len(words[j]) {
            return words[i] < words[j]
        }
        return len(words[i]) > len(words[j])
    })
    return words[0]
}



