for i := len(word) - 1; i >= 0; i-- {
    if string(word[i]) == "a" || string(word[i]) == "e" || string(word[i]) == "i" || string(word[i]) == "o" || string(word[i]) == "u" {
        return string(word[i])
    }
    if string(word[i]) != "a" && string(word[i]) != "e" && string(word[i]) != "i" && string(word[i]) != "o" && string(word[i]) != "u" {
        continue
    }
    if i == 0 {
        return ""
    }
}
return ""
}