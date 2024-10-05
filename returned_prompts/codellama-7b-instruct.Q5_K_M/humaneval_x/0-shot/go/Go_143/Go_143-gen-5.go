for i := 1; i <= len(sentence); i++ {
    if strings.Contains(sentence, " ") {
        words := strings.Split(sentence, " ")
        for j := 0; j < len(words); j++ {
            if len(words[j]) != i {
                continue A
            }
        }
        return sentence
    }
}
return ""
}