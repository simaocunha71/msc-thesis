    type letterCounter struct {
        S        string
        Counts   map[rune]int
    }
    counts := make([]letterCounter, 0)
    for _, s := range words {
        counts = append(counts, letterCounter{
            S:        s,
            Counts:   make(map[rune]int),
        })
        for _, r := range s {
            if _, ok := counts[len(counts)-1].Counts[r]; ok {
                counts[len(counts)-1].Counts[r]++
            } else {
                counts[len(counts)-1].Counts[r] = 1
            }
        }
    }
    max := counts[0]
    for i := 1; i < len(counts); i++ {
        if len(counts[i].Counts) > len(max.Counts) {
            max = counts[i]
        } else if len(counts[i].Counts) == len(max.Counts) && counts[i].S < max.S {
            max = counts[i]
        }
    }
    return max.S
}



