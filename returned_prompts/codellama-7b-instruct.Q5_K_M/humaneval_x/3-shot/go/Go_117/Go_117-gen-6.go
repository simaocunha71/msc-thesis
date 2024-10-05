    var words []string

    var word_buffer bytes.Buffer
    var word_length int
    var is_word_char bool

    for _, c := range s {

        if c == ' ' {
            if word_length == n {
                words = append(words, word_buffer.String())
            }
            word_buffer.Reset()
            word_length = 0
            is_word_char = false
        } else {
            word_length += 1
            word_buffer.WriteRune(c)
            is_word_char = true
        }
    }

    if word_length == n {
        words = append(words, word_buffer.String())
    }

    return words
}



