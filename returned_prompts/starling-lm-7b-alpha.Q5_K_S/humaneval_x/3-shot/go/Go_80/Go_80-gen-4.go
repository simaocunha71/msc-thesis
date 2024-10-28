    if len(s) < 3 {
        return false
    }

    var index int = 0
    var set = make(map[rune]bool)
    for {
        if _, ok := set[rune(s[index])]; ok {
            return false
        } else {
            set[rune(s[index])] = true
        }
        if index > len(s)-2 {
            return true
        }
        index += 1
    }
}



