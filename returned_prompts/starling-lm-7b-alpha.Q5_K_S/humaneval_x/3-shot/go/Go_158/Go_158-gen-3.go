    type CharCount struct {
        Count int
        Word  string
    }
    result := CharCount{
        Count: 0,
        Word:  "",
    }

    for _, word := range words {
        charCount := CharCount{
            Count: 0,
            Word:  word,
        }
        for _, c := range word {
            charCount.Count += 1
            if charCount.Count > result.Count {
                result = charCount
            }else if charCount.Count == result.Count {
                if charCount.Word < result.Word {
                    result = charCount
                }
            }
        }
    }
    return result.Word
}



