    words := strings.Fields(s)
    sort.Sort(sort.StringSlice(words))
    return strings.Join(words, " ")
}



