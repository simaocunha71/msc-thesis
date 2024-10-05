    for i := len(word) - 2; i > 0; i-- {
        if !IsVowel(word[i]) && IsVowel(word[i+1]) && IsVowel(word[i-1]) {
            return string(word[i])
        }
    }
    return ""
}

func IsVowel(c byte) bool {
    switch bytes.ToLower([]byte{c})[0] {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    default:
        return false
    }
}



A: 
import "unicode"

func GetClosestVowel(word string) string {
    vowels := map[rune]struct{}{
        'a': {}, 'e': {}, 'i': {}, 'o': {}, 'u': {},
        'A': {}, 'E': {}, 'I': {}, 'O': {}, 'U': {},
    }
    var prev, next rune
    for i := len(word) - 1; i > 0; i-- {
        prev, next = rune(word[i-1]), rune(word[i+1])
        if _, ok := vowels[rune(word[i])]; !ok &&
            _, ok := vowels[prev] && _, ok := vowels[next] {
            return string(rune(word[i]))
        }
    }
    return ""
}


A: Here is