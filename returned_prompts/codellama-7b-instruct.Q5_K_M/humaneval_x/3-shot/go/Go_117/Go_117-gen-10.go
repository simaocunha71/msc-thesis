    result := make([]string, 0)
    if len(s) == 0 {
        return result
    }
    var current_word string
    var current_length int
    for _, c := range s {
        if c == ' ' {
            if current_length == n {
                result = append(result, current_word)
            }
            current_word = ""
            current_length = 0
        } else if is_cons(c) {
            current_length += 1
            current_word += string(c)
        }
    }
    if current_length == n {
        result = append(result, current_word)
    }
    return result
}

func is_cons(c rune) bool {
    return !is_vow(c)
}

func is_vow(c rune) bool {
    return strings.ContainsRune("aeiou", c)
}



