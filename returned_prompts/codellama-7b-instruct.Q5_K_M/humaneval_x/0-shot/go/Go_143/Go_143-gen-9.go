for _, word := range strings.Split(sentence, " ") {
    for i := 2; i <= len(word); i++ {
        if i%2 == 0 {
            continue A
        }
    }
    return word
}
return ""
}
