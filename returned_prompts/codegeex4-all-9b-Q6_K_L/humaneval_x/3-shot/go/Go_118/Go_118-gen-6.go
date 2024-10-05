    vowels := []string{"A","E","I","O","U","a","e","i","o","u"}
    result := ""
    for i := len(word)-1; i >= 0; i-- {
        if !IsConsonant(string(word[i])){
            continue
        }
        for j := i-1; j >= 0; j-- {
            if IsVowel(string(word[j])){
                result = string(word[j])
                break
            }
        }
        break
    }
    return result
}
func IsConsonant(c string) bool {
    consonants := []string{"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
        "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
    for _, v := range consonants {
        if v == c {
            return true
        }
    }
    return false
}
func IsVowel(c string) bool {
    vowels := []string{"A","E","I","O","U","a","e","i","o","u"}
    for _, v := range vowels {
        if v == c {
            return true
        }
    }
    return false
}

