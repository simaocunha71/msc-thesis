    type CharCount struct {
        Count int
        Word  string
    }

    result := make(map[string]CharCount)
    for _, word := range words {
        for _, c := range word {
            if _, ok := result[c]; ok {
                result[c].Count += 1
            } else {
                result[c] = CharCount{Count: 1, Word: word}
            }
        }
    }
    sorted_result := make([]CharCount, 0)
    for _, v := range result {
        sorted_result = append(sorted_result, v)
    }
    sort.Slice(sorted_result, func(i, j int) bool {
        return sorted_result[i].Count < sorted_result[j].Count ||
            (sorted_result[i].Count == sorted_result[j].Count &&
                sorted_result[i].Word < sorted_result[j].Word)
    })
    return sorted_result[len(sorted_result)-1].Word
}



