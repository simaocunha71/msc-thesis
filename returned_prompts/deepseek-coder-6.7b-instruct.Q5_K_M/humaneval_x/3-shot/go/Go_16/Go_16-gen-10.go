    str = strings.ToLower(str)
    distinctCharacters := make(map[rune]bool)

    for _, c := range str {
        distinctCharacters[c] = true
    }

    return len(distinctCharacters)
}



