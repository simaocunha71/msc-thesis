    v := make([]string,0)
    for _, w := range strings.Fields(s) {
        if CountConsonants(w) == n {
            v = append(v, w)
        }
    }
    return v
}

func CountConsonants(s string) int {
    v := 0
    for _, r := range s {
        if !IsVowel(r) {
            v += 1
        }
    }
    return v
}

func IsVowel(r rune) bool {
    switch strings.ToLower(string(r)) {
    case "a", "e", "i", "o", "u":
        return true
    default:
        return false
    }
}





