    type unique_chars struct {
        chars []rune
        count int
    }
    type by_count []unique_chars
    by_count.Len = func(i, j int) int {
        return by_count[i].count - by_count[j].count
    }
    by_count.Swap = func(i, j int) {
        by_count[i], by_count[j] = by_count[j], by_count[i]
    }

    result := ""
    max_count := 0

    for _, word := range words {
        unique_word := make(map[rune]bool)
        for _, char := range word {
            unique_word[char] = true
        }
        unique_chars_slice := []unique_chars{}
        for char, _ := range unique_word {
            unique_chars_slice = append(unique_chars_slice, unique_chars{
                chars: []rune{char},
                count: 1,
            })
        }
        sort.Sort(by_count(unique_chars_slice))

        if len(unique_chars_slice) > max_count {
            max_count = len(unique_chars_slice)
            result = word
        }else if len(unique_chars_slice) == max_count {
            if word < result {
                result = word
            }
        }
    }
    return result
}



