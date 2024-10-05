for i := len(word) - 1; i >= 0; i-- {
    if word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u' {
        return string(word[i])
    }
}

return ""
}
