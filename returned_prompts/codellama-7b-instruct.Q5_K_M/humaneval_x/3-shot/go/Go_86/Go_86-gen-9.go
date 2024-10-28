    words := strings.Split(s, " ")
    sort.Slice(words, func(i, j int) bool {
        return words[i] < words[j]
    })

    return strings.Join(words, " ")
}



