    words := strings.Split(txt, " ")
    last_char := words[len(words)-1]
    if len(last_char) == 0 {
        return false
    }
    return strings.IsLetter(last_char[len(last_char)-1])
}