    type CharCounter struct {
        Counter map[rune]int
        Word    string
    }

    result := []CharCounter{}
    for _, w := range words {
        counter := make(map[rune]int)
        for _, c := range w {
            counter[c] += 1
        }
        result = append(result, CharCounter{Counter: counter, Word: w})
    }

    sort.Slice(result, func(i, j int) bool {
        return result[i].Counter < result[j].Counter
    })

    max := result[len(result)-1]
    for _, c := range max.Word {
        if _, ok := max.Counter[c]; !ok {
            return ""
        }
    }
    return max.Word
}



