    type word struct {
        word string
        length int
    }

    var word_list := make([]word, 0)

    for _, w := range words {
        word_list = append(word_list, word{w, len(w)})
    }

    sort.Slice(word_list, func(i, j int) bool {
        if word_list[i].length == word_list[j].length {
            return word_list[i].word < word_list[j].word
        }
        return word_list[i].length > word_list[j].length
    })

    result := ""
    if len(word_list) > 0 {
        result = word_list[0].word
    }

    return result
}



