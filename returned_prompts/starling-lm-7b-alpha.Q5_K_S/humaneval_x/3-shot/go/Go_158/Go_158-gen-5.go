    type UniqueCharacters struct {
        Count int
        Characters []rune
    }

    type ByCount struct {
        Count int
    }

    type ByLexicographicalOrder struct {
        Characters []rune
    }

    result := make([]UniqueCharacters, 0)
    for _, word := range words {
        unique_characters := make(map[rune]bool)
        for _, c := range word {
            unique_characters[c] = true
        }
        result = append(result, UniqueCharacters{
            Count: len(unique_characters),
            Characters: make([]rune, 0, len(unique_characters)),
        })

        for c := range unique_characters {
            result[len(result)-1].Characters = append(result[len(result)-1].Characters, c)
        }
    }

    sort.Slice(result, func(i int, j int) bool {
        return ByCount{result[i].Count}.Count > ByCount{result[j].Count}.Count
    })

    if len(result) == 1 {
        return result[0].Characters[0]
    }

    sort.Slice(result, func(i int, j int) bool {
        return ByLexicographicalOrder{result[i].Characters}.Characters < ByLexicographicalOrder{result[j].Characters}.Characters
    })

    return result[0].Characters[0]
}





