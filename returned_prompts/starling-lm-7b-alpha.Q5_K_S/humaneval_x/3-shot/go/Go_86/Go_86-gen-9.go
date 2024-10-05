    words := strings.Split(s, " ")
    new_words := make([]string, len(words))
    for i := 0; i < len(words); i++ {
        new_words[i] = Shuffle(words[i])
    }
    return strings.Join(new_words, " ")
}

func Shuffle(s string) string {
    var result string
    for _, c := range s {
        result = result + string(sort.IntSlice([]int{int(c)}).Slice())
    }
    return result
}



