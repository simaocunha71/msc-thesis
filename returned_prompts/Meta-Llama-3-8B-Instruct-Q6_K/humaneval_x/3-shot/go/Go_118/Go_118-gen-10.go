    var result string
    for i := len(word) - 1; i > 0; i-- {
        if "aeiouAEIOU"[0] <= byte(word[i]) && byte(word[i]) <= "aeiouAEIOU"[4] {
            result = string(word[i])
            return result
        }
    }
    return result
}