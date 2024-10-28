    var i int = len(word) - 1
    for i >= 0 {
        if string(word[i]) == "a" || string(word[i]) == "e" || string(word[i]) == "i" || string(word[i]) == "o" || string(word[i]) == "u" {
            return string(word[i])
        }
        if string(word[i]) != "a" && string(word[i]) != "e" && string(word[i]) != "i" && string(word[i]) != "o" && string(word[i]) != "u" {
            i = i - 1
        }
    }
    return ""
}



