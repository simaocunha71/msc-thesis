    last_char := strings.TrimSpace(txt)
    last_char = last_char[len(last_char)-1:]
    return strings.IsLetter(last_char[0]) && !strings.Contains(last_char, " ")
}