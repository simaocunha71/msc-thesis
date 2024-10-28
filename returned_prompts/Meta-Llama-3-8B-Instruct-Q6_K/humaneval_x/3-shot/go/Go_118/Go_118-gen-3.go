    var result string
    for i := len(word) - 1; i >= 0; i-- {
        if "aeiouAEIOU".indexOf(word[i]) != -1 {
            if i < len(word) - 1 && "aeiouAEIOU".indexOf(word[i+1]) == -1 {
                result = string(word[i])
                break
            }
        }
    }
    return result
}