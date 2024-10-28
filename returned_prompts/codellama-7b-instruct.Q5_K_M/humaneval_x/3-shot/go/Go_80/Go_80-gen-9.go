    if len(s) < 3 {
        return false
    }

    var unique_chars map[rune]bool
    unique_chars = make(map[rune]bool)

    for i := 0; i < len(s); i++ {
        if _, ok := unique_chars[s[i]]; !ok {
            unique_chars[s[i]] = true
        }else{
            return false
        }

        if len(unique_chars) == len(s) {
            return true
        }
    }

    return false
}



