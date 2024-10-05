    var max = ""
    for _, word := range words {
        if len(unique(word)) > len(unique(max)) {
            max = word
        } else if len(unique(word)) == len(unique(max)) {
            if lexicographicallyFirst(word, max) {
                max = word
            }
        }
    }
    return max
}

func unique(word string) []byte {
    unique := []byte{}
    for _, r := range word {
        if !contains(unique, r) {
            unique = append(unique, r)
        }
    }
    return unique
}

func contains(list []byte, value byte) bool {
    for _, v := range list {
        if v == value {
            return true
        }
    }
    return false
}

func lexicographicallyFirst(a, b string) bool {
    for i := 0; i < len(a); i++ {
        if a[i] != b[i] {
            return a[i] < b[i]
        }
    }
    return len(a) < len(b)
}













































































































































































































































