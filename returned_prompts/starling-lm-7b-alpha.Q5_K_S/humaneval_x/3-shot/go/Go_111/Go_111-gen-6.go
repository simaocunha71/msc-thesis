    hist := make(map[rune]int)

    for _, letter := range test {
        hist[letter]++
    }

    return hist
}



