    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i := 0; i < len(word); i++ {
        if vowels[0] == word[i] || vowels[1] == word[i] || vowels[2] == word[i] || vowels[3] == word[i] || vowels[4] == word[i]
        || vowels[5] == word[i] || vowels[6] == word[i] || vowels[7] == word[i] || vowels[8] == word[i] || vowels[9] == word[i] {
            return string(word[i])
        }
    }
    buffer := bytes.Buffer{}
    for i := len(word) - 1; i >= 0; i-- {
        if vowels[0] == word[i] || vowels[1] == word[i] || vowels[2] == word[i] || vowels[3] == word[i] || vowels[4] == word[i]
        || vowels[5] == word[i] || vowels[6] == word[i] || vowels[7] == word[i] || vowels[8] == word[i] || vowels[9] == word[i] {
            buffer.WriteString(string(word[i]))
        }
    }

    for i := 0; i < len(buffer.String()); i++ {
        if vowels[0] == buffer.String()[i] || vowels[1] == buffer.String()[i] || vowels[2] == buffer.String()[i] || vowels[3] == buffer.String()[i] || vowels[4] == buffer.String()[i]
        || vowels[5] == buffer.String()[i] || vowels[6] == buffer.String()[i] || vowels[7] == buffer.String()[i] || vowels[8] ==