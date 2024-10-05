    if len(word) <= 2 {
        return ""
    }

    var last_char_index int
    for i := len(word) - 2; i >= 0; i-- {
        if "aeiou"[bytes.IndexByte([]byte("aeiou"), word[i])] != byte(0) {
            last_char_index = i
            break
        }
    }

    if last_char_index == 0 {
        return ""
    }

    var next_char_index int
    for i := last_char_index + 1; i < len(word); i++ {
        if "aeiou"[bytes.IndexByte([]byte("aeiou"), word[i])] != byte(0) {
            next_char_index = i
            break
        }
    }

    if next_char_index == len(word) - 1 {
        return ""
    }

    return string(word[last_char_index+1])
}



