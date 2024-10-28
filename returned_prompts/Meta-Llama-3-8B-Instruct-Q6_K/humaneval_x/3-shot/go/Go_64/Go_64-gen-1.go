    vowels := "aeiouAEIOUY"
    count := 0
    for _, c := range s {
        if strings.IndexRune(vowels, c) != -1 {
            count++
        }
    }
    return count
}
