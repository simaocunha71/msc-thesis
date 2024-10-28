    v := make([]string, 0)
    for _, w := range strings.Fields(s) {
        c := 0
        for _, b := range []rune(w) {
            if !isVowel(b) {
                c += 1
            }
            if c > n {
                break
            }
        }
        if c == n {
            v = append(v, w)
        }
    }
    return v
}

func isVowel(b rune) bool {
    switch strings.ToLower(string(b)) {
    case "a", "e", "i", "o", "u":
        return true
    }
    return false
}



