    type CharCount struct {
        Value string
        Count int
    }

    counts := make([]CharCount, 0)

    for _, word := range words {
        counts = append(counts, CharCount{Value: word, Count: len(word)})
    }

    sort.Slice(counts, func(i, j int) bool {
        if counts[i].Count != counts[j].Count {
            return counts[i].Count > counts[j].Count
        }else {
            return counts[i].Value < counts[j].Value
        }
    })

    return counts[0].Value
}



