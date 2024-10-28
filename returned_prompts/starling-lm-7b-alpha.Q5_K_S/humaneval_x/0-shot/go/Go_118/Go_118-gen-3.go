    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    result := ""
    var i int
    for i = 0; i < len(word); i++ {
        if !isConsonant(word[i]) {
            continue
        }
        for j := i + 1; j < len(word); j++ {
            if !isConsonant(word[j]) {
                result = string(word[j])
                break
            }
        }
    }
    for _, v := range vowels {
        if isVowel(v) && result == "" {
            result = string(v)
        }
    }
    return result
}

func isConsonant(char rune) bool {
    return char != 'a' && char != 'e' && char != 'i' && char != 'o' && char != 'u' && char != ' '
}

func isVowel(char rune) bool {
    return char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u'
}

/*
GetClosestVowel("yogurt") return "u"
GetClosestVowel("FULL") return "U"
GetClostestVowel("quick") return ""
GetClosestVowel("ab") return ""
*/

// Another approach
func GetClosestVowel2(word string) string {
    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    result := ""
    for _, v := range vowels {
        if isVowel(v) && result == "" {
            for i := len(word) - 1; i > 0; i-- {
                if !isConsonant(word[i]) {
                    result = string(v)
                    break
                }
            }
        }
    }
    return result
}

func isConsonant(char rune) bool {
    return char != 'a' && char != 'e' && char !=