    words := strings.Split(s," ")
    new_words := make([]string,len(words))

    for i,word := range words {
        new_words[i] = AntiShuffleWord(word)
    }
    return strings.Join(new_words," ")
}

func AntiShuffleWord(s string) string {
    sorted := make([]rune,len(s))
    for i,char := range s {
        sorted[i]=char
        sort.Slice(sorted[:i+1],func(i,j int) bool {
            return rune(sorted[i])<rune(sorted[j])
        })
    }
    return string(sorted)
}



